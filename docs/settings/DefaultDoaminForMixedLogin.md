# Default Domain For Mixed Login

**Technical Name:** DefaultDoaminForMixedLogin

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

The Default Domain For Mixed Login parameter is used to predefine a domain in environments where authentication methods are mixed, specifically within the Pathlock Cloud GRC platform. This parameter is crucial for identifying the default domain during user login processes where authentication could be either Windows-based or another method.

**Business Impact:**

Setting a default domain simplifies the login process for users by eliminating the need to input their domain name. This is particularly beneficial in mixed-authentication environments, enhancing user experience, and reducing the time taken for users to access the system. It streamlines access for users across different departments and geographies, thereby improving overall system efficiency and user satisfaction.

**Technical Impact when configured:**

When configured, the system automatically prefixes the defined default domain to user logins in mixed authentication modes. This auto-configuration helps in reducing login errors related to domain specification, leading to fewer support tickets and a smoother login process.

**Examples Scenario:**

- **Scenario 1:** In an organization using both Windows authentication and Form-based authentication, configuring the Default Domain For Mixed Login as "CORP" allows users to log in with just their username without the need to specify "CORP\" every time. This not only speeds up the login process but also ensures consistency in user credentials across systems.

**Related Settings:** 

- **LoginMethod** (as seen in the code with reference to mixed authentication modes)

**Best Practices:** 

- **Configure when:** your environment utilizes mixed-mode authentication and you want to streamline the login process.
- **Avoid when:** your organization has strict policies requiring users to explicitly specify their domain during login or when only a single authentication mode is in use.