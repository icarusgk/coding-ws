class Person {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`Hello there! My name is ${this.name}`);
  }
}

class Doctor extends Person {
  constructor(name) {
    super(name);
  }

  speak() {
    super.speak();
    console.log(`and I'm a doctor!`);
  }
}

const roger = new Person("Roger");
const bryan = new Doctor("Bryan");

roger.speak();
bryan.speak();