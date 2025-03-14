# CreateNewDoctorUsernamePatternForVMA

## Category
New Employees Creation

## Default Value
The default value is obtained dynamically from the system's resources and may vary based on installation configuration.

## Impact Level
Medium

## Description
The `CreateNewDoctorUsernamePatternForVMA` parameter is used within the Pathlock Cloud GRC platform for configuring the username pattern for newly created Virtual Medical Assistant (VMA) accounts specifically tailored for doctors. This parameter influences how the VMA user accounts are generated, ensuring they align with organizational standards and compliance requirements.

## Business Impact
The configuration of this parameter has a significant impact on the organization's ability to efficiently onboard new medical professionals into their system. A well-defined username pattern can streamline user account setup, reduce administrative overhead, enhance system security, and ensure a consistent user identity management strategy that complies with regulatory standards.

## Technical Impact when configured
- **Enhanced Security:** By standardizing the username format, it becomes easier to manage access controls and permissions, thereby reducing the risk of unauthorized access.
- **Operational Efficiency:** Automated username generation based on a predefined pattern can significantly speed up the account creation process for new doctors.
- **Compliance:** Helps in maintaining compliance with IT security policies and external regulatory requirements concerning user account management.

## Examples Scenario

- **Onboarding New Doctors:** When a new doctor is onboarded, their VMA account needs to be created. By defining a username pattern (e.g., first initial + last name), the system automatically generates the username, ensuring consistency and saving time.

## Related Settings
- `CreateNewDoctorSapSystemId`: This setting specifies the system ID for the doctor's SAP system, which often works in tandem with the username pattern to ensure compatibility and cohesiveness across different systems.

## Best Practices
- **Configure When:** You are setting up the Pathlock platform for a medical institution or updating the account creation policies to meet new compliance standards.
- **Avoid When:** If your organization does not require a standardized username pattern or if the pattern could infringe upon privacy regulations or create unnecessary complexity.

## Context
Within the Pathlock Cloud GRC platform, especially in environments that manage Virtual Medical Assistants, configuring the `CreateNewDoctorUsernamePatternForVMA` parameter is crucial for secure and efficient user identity management. The parameter is specifically designed to cater to the needs of the healthcare sector by providing a standardized approach to creating usernames for doctor's VMA accounts, thus aiding in smooth operational transitions and secure access management.