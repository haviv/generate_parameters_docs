# CreateNewDoctorSapSystemId Parameter Documentation

## Category
Configuration/Setup

## Default Value
Not explicitly mentioned, but it uses a default value set in `CommonSettings`.

## Impact Level
High

## Description
The `CreateNewDoctorSapSystemId` parameter defines the SAP System ID used when creating new doctor profiles within the Pathlock Cloud GRC platform. This ID is pivotal in determining the correct SAP system environment for which the new profiles will be configured.

## Business Impact
- Ensures that new doctor profiles are created in the correct SAP system, aligning with organizational policies and system architectures.
- Improves compliance and data integrity by ensuring that sensitive medical personnel data is handled in the designated secured environment.
- Streamlines the process of onboarding new doctors by automatically configuring their profiles in the correct system, reducing manual errors and administrative overhead.

## Technical Impact when configured
- Initializes the ProfileTailorContext with the specific SAP System ID, directing all subsequent actions (such as creating and configuring new doctor profiles) to the specified SAP system.
- Helps in maintaining a centralized, consistent approach to handle SAP system connections across different workflow actions like `GetOrCreateVMAUser` and `CreateNewDoctor`.

## Example Scenario
An administrator wishes to onboard a new doctor into their healthcare organization's SAP system. By setting the `CreateNewDoctorSapSystemId` to their specific healthcare-related SAP system ID, they ensure that the onboarding process, including the creation of SAP roles and permissions for the new doctor, occurs in the correct SAP environment. This is especially critical in healthcare settings where access to specific patient data and medical systems is restricted and closely monitored for compliance with regulations like HIPAA.

## Related Settings
- `CommonSettings.Default` (for obtaining the default system-wide settings)
- SAP Connector configurations (for setting up and managing connections to SAP systems)

## Best Practices
- **Configure when:** Setting up the platform for the first time or adding new SAP systems that will involve the creation of new doctor profiles.
- **Avoid when:** If there is no clear separation of SAP systems within your organization, or when the configured SAP System ID no longer exists or has been changed.

Understanding and correctly setting the `CreateNewDoctorSapSystemId` ensures that the healthcare professionals' digital onboarding and subsequent data handling are executed within the correct system environment, thereby safeguarding compliance, data integrity, and operational efficiency.