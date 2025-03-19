# Generate Username

**Category:** User Management

**Description:** This action focuses on generating a username for new users by applying a set of predefined patterns and rules. The process involves extracting and manipulating specific parts of user information like first name, last name, etc., to form a unique identifier for each user. This identifier can then be used across the Pathlock Cloud platform. The workflow goes through different phases, including deciding on the pattern to use, applying character limitations, adding prefixes, and adjusting the case of the generated username.

**Parameters:** 

- Basic:
    - Name: FirstName
    - Description: The first name of the user, which is used as a base for generating the username.
    - Default value: None
    - Mandatory: Yes
  
    - Name: LastName
    - Description: The last name of the user, which can be utilized in generating the username based on the configured patterns.
    - Default value: None
    - Mandatory: No

- Advanced:
    - Name: Prefix
    - Description: An optional prefix to be added before the username. It is used in specific patterns to create a more distinguishable or branded username.
    - Default value: None
    - Mandatory: No
  
    - Name: FieldLength
    - Description: Controls the length of the particular field to be used in the username. Allows for trimming or limiting the size of the username's part derived from user attributes.
    - Default value: None
    - Mandatory: No
  
    - Name: SkipChars
    - Description: Determines the number of characters to skip from the beginning of the field value. Useful for generating usernames that avoid common prefixes or undesired characters.
    - Default value: None
    - Mandatory: No
  
    - Name: IsFieldUpperCase
    - Description: A boolean parameter that, when true, converts the relevant part of the username to uppercase, facilitating readability and standardization in certain patterns.
    - Default value: False
    - Mandatory: No

**Business impact:** Generating usernames is a critical part of user management and identity recognition within the Pathlock Cloud platform. By automating this process, the platform enhances usability, reduces manual errors, and ensures that user identities are managed systematically. This capability directly impacts the ease of access management, security policy enforcement, and overall governance within the system.

**Example of usage:** To generate a username for a new user named "Yoav Michaeli" with a preference for an uppercase first character of the first name, and the full last name in lowercase, followed by a "_corp" suffix for corporate accounts, the following patterns could be configured:

1. First letter of FirstName in uppercase.
2. Full LastName in lowercase.
3. Append "_corp" as a prefix.

The generated username could be "Ymichaeli_corp".

**Prerequisites:** Before executing this action, ensure that:

- The user information (at least the first name) is available and accurately entered.
- The username generation patterns are predefined and configured in accordance with corporate standards and requirements.
- Necessary permissions for generating and assigning usernames are granted to the executing entity.

**Error Handling and Troubleshooting:** 

- If a username fails to generate:
    - **Cause:** Missing user information (e.g., FirstName, LastName).
    - **Solution:** Verify that all required information is provided and correctly spelled.
    
- If the generated username does not meet expected formats:
    - **Cause:** Misconfiguration of the username patterns (e.g., incorrect FieldLength, SkipChars settings).
    - **Solution:** Review and adjust the configured patterns to ensure they meet the organization's naming standards.
    
- If the action cannot be executed:
    - **Cause:** Insufficient privileges.
    - **Solution:** Ensure the user or system executing the action has the necessary permissions to generate and assign usernames.