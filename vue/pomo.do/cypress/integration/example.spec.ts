// https://docs.cypress.io/api/introduction/api.html

// Basic Cypress test
describe("My First Test", () => {
  it("visits the app root url", () => {
    cy.visit("/");
    cy.contains("h1", "You did it!");
  });
});
