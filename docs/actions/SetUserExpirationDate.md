# SetUserExpirationDate

**Category:** User Management

**Description:** 

The `SetUserExpirationDate` action is designed to manage user account validity within the Pathlock Cloud platform, particularly focusing on the expiration of user accounts. It leverages parameters to calculate and set expiration dates for users, optionally updating action text and handling user lock reasons based on the specified expiration or validity date. This action supports conditional logic for handling dates directly specified by the user, defaults, or calculated based on a number of days until expiration. Additionally, it incorporates functionality to clear a user's validity under specific conditions, providing flexibility for account management strategies.

**Parameters:**

Basic:
- Name: TechnicalNameForDaysUntilExpiration
  Description: Specifies the number of days until a user account should expire. This parameter is used to calculate the expiration date from the current date.
  Default value: N/A
  Mandatory: No
  
- Name: UserValidityDateFormat
  Description: Defines the custom format for the UserValidityDate parameter, allowing for precise date formatting according to business requirements.
  Default value: N/A
  Mandatory: No

- Name: UserValidityDate
  Description: Directly specifies the expiration date for the user account, which can be defined in a custom format as dictated by the UserValidityDateFormat parameter.
  Default value: N/A
  Mandatory: No
  
- Name: ClearUserValidity
  Description: A boolean parameter that, when true, indicates the user’s validity should be cleared. This is typically used in scenarios where an account is being closed or deactivated.
  Default value: false
  Mandatory: No
  
Advanced:
- Name: OverrideValidityDate
  Description: Allows the specification of an alternate expiration date, overriding other parameters if set.
  Default value: N/A
  Mandatory: No

**Business impact:**

The `SetUserExpirationDate` action significantly impacts the management of user lifecycles within the Pathlock Cloud platform, facilitating automated account deactivation, reactivation, and maintenance tasks. It aids in enforcing access policies by ensuring that user access rights expire at appropriate times, thereby enhancing security and compliance with internal and external regulations.

**Example of usage:**

A common scenario involves setting an expiration date for a contractor's account to ensure the account is automatically deactivated upon contract completion. By specifying the `TechnicalNameForDaysUntilExpiration` parameter, the contractor’s user account can be set to expire, for example, 30 days from the current date, effectively limiting access after the contract period without manual intervention.

**Prerequisites:**

1. Administrative permissions to manage user accounts within the Pathlock Cloud platform.
2. A valid user context, indicating the user account to which the expiration date changes will apply.

**Error Handling and Troubleshooting:**

- **Common Error Scenario:** Invalid Date Format Error
  - **Probable Cause:** The `UserValidityDate` parameter is provided in an incompatible format not matching the specified `UserValidityDateFormat`.
  - **Solution:** Ensure the date format specified in `UserValidityDateFormat` accurately reflects the format of the date provided in `UserValidityDate`.

- **Common Error Scenario:** Failure to Update Expiration Date
  - **Probable Cause:** Lack of permissions to modify user account details or an incorrect user context.
  - **Solution:** Verify that the executing account has the necessary permissions to modify user details and that the user context is correctly specified.