export const REGISTER_MUTATION = `
mutation RegisterUser(
    $Username: String!,
    $Email: String!,
    $Password: String!
) {
    RegisterUser(
      input: {
        Username: $Username,
        Email: $Email,
        Password: $Password
      }
    ) {
        Username
        Email
        Password
    }
} 
`;

export const LOGIN_MUTATION = `
mutation LoginUser(
    $Email: String!,
    $Password: String!
) {
    LoginUser(
      input: {
        Email: $Email,
        Password: $Password
      }
    ) {
        Email
        Password
    }
} 
`;