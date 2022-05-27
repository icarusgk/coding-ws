import React from 'react';
import { fetchUserData, cancelFetch } from './dataFetcher';
import { Userlist } from './Userlist';

export class Profile extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      userData: null
    }
  }
  loadUserData() {
    this.setState({ userData: null });
    this.fetchID = fetchUserData(this.props.username, userData => {
      this.setState({ userData });
    });
  }

  componentDidMount() {
    this.loadUserData();
  }
  componentDidUpdate(prevProps) {
    if (this.props.username === prevProps.username) return;
    cancelFetch(this.fetchID);
    this.loadUserData();
  }
  componentWillUnmount() {
    cancelFetch(this.fetchID);
  }
  render() {
    const isLoading = !this.state.userData;

    let className = 'Profile';
    if (isLoading) {
      className += ' loading';
    }

    return (
      <div className={className}>
        <div className="profile-picture">
          {!isLoading && <img
            src={this.state.userData.profilePictureUrl}
            alt=""
          />}
        </div>
        <div className="profile-body">
          <h2>{isLoading ? "Loading" : this.state.userData.name}</h2>
          <h3>@{this.props.username}</h3>
          <p>{isLoading ? "Loading" : this.state.userData.bio}</p>
          <h3>My friends</h3>
          <Userlist usernames={isLoading ? [] : this.state.userData.friends} onChoose={this.props.onChoose} />
        </div>
      </div>
    );
  }
}