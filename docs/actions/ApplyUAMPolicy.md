# ApplyUAMPolicy

**Category:** User Management

**Description:** 

The `ApplyUAMPolicy` action is designed to automate the application of User Access Management (UAM) policies to specific policy groups within the Pathlock Cloud platform. When executed, this action iterates over a list of provided policy group names, deploying relevant UAM policies for each. If no specific policy groups are provided, the action will apply UAM policies across the board. This process is vital in ensuring that access rights and permissions within the system are kept up to date according to the defined access policies, contributing to stronger security and compliance postures.

**Parameters:**

- **Basic Parameters**:
    - Name: `PolicyGroupTechnicalName`
    - Description: A comma-separated list of technical names identifying the policy groups for which UAM policies should be applied. This parameter drives the selection of policy groups that will be processed. If left empty or unspecified, UAM policies will be applied across all available policy groups.
    - Default value: *(empty string)*
    - Mandatory: No

**Business impact:** 

Applying UAM policies effectively ensures that access permissions and rights are consistently enforced across the organization's digital assets, minimizing the risk of unauthorized access and potential security breaches. It aids in compliance with internal and external governance, risk management, and compliance (GRC) requirements by automating the enforcement of access controls. For businesses, this means reduced operational risks and enhanced security postures.

**Example of usage:** 

An administrator wants to apply new UAM policies to the "HR" and "Finance" policy groups after an update in access management procedures. By specifying these policy groups in the `ApplyUAMPolicy` action, the platform will ensure that these specific areas are immediately updated to reflect the latest access controls, without the need to manually review and apply policies.

**Prerequisites:** 

Users must have administrative rights to manage UAM policies within the Pathlock platform. Additionally, there should be a clear understanding of the policy groups in existence and their corresponding technical names to correctly use this action.

**Error Handling and Troubleshooting:** 

- **Error:** Policies not applying to specified policy groups.
    - **Cause:** Incorrect technical names used for policy groups.
    - **Solution:** Verify the technical names of the policy groups intended for the policy application. Make sure they match exactly with those defined within the system.
   
- **Error:** Action applies policies to all groups despite specifying policy groups.
    - **Cause:** Incorrect formatting or delimitation of the policy group names in the input parameter.
    - **Solution:** Ensure that policy group names are correctly separated by commas without spaces. Review the format and retry the operation.

In instances where issues persist after attempting the recommended solutions, consult the platform's support documentation or contact technical support for further assistance.