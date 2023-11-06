it("API endpoint test", () => {
  cy.request(
    "GET",
    "https://fra90a3sa5.execute-api.us-east-1.amazonaws.com/PROD/"
  ).should((response) => {
    expect(response.status).to.eq(500);
  });
});
