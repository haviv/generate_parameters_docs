Action name: Set User SoD Violation Status

**Category:** Compliance

**Description:** 

The Set User SoD (Segregation of Duties) Violation Status action is designed to update or clear the status of a user's Segregation of Duties violation within the Pathlock Cloud platform. This action takes into account the specific violation either by directly specifying the violation or deriving it from the associated event and user context. The action evaluates whether to update the violation status with a new value or clear it, based on the parameters provided. This process helps in managing the compliance status related to SoD within an organization, allowing for a dynamic response to risk calculation and mitigation processes.

**Parameters:** 

Basic:

- **Name:** combinationName
  - **Description:** Specifies the name of the SoD violation to be mitigated. This parameter is used to identify the specific violation if the combination ID is not directly provided or derived from an event.
  - **Default value:** None
  - **Mandatory:** No

- **Name:** SodRiskStatus
  - **Description:** The status to be set for the identified SoD violation. This can be any value from the predefined SoD risk statuses in the Pathlock Cloud platform, determining the current compliance state of the violation.
  - **Default value:** None
  - **Mandatory:** No

Advanced:

- **Name:** ClearStatus
  - **Description:** A boolean parameter that specifies whether to clear the existing status of the SoD violation. When set to true, the action attempts to remove any previously set status, effectively resetting the violation status.
  - **Default value:** false
  - **Mandatory:** No

**Business impact:** 

This action plays a crucial role in maintaining and enforcing compliance within the organization's IT environment. By managing the status of SoD violations, Pathlock Cloud enables organizations to dynamically adjust their compliance posture in response to internal audits or changes in compliance standards. Effective management of SoD violations helps prevent unauthorized access and reduces the risk of fraud, ensuring that internal controls are properly enforced.

**Example of usage:** 

This action could be triggered as part of a scheduled compliance review process, where an administrator sets or clears violation statuses based on the results of the review. Alternatively, it may be executed in response to a detected event indicating a potential SoD violation, where the system automatically updates the violation status based on predefined rules and conditions.

**Prerequisites:** 

- The user must have appropriate permissions to manage SoD violation statuses within Pathlock Cloud.
- A valid user and violation context must be available for the action to be executed correctly.

**Error Handling and Troubleshooting:** 

- **Common Error:** Failure to resolve the status parameter.
  - **Probable Cause:** The SodRiskStatus parameter was not provided or is invalid.
  - **Recommended Solution:** Verify that a valid SodRiskStatus parameter value is passed. If dynamic, ensure the workflow context contains a valid status value.

- **Common Error:** Violation not found.
  - **Probable Cause:** The specified combinationName or derived combination ID does not match any recorded SoD violation.
  - **Recommended Solution:** Verify the accuracy of the combinationName parameter and the integrity of event data used to derive violation IDs.