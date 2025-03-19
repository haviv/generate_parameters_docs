# MitigateUserSodViolation

**Category:** Risk Management

**Description:** The MitigateUserSodViolation action is designed to manage and mitigate Segregation of Duties (SOD) violations for users within the Pathlock platform. This workflow action allows for either the extension of mitigation for already approved risks or the initiation of new mitigation processes. The flow involves identifying the user and violation combination, determining the mitigation duration, and optionally extending an already approved risk mitigation based on a set of parameters provided at execution.

**Parameters:**

- Basic:
    - Name: mitigateDaysNum
      Description: Specifies the number of days for which the SOD violation mitigation is to be extended.
      Default value: N/A
      Mandatory: No
      
    - Name: fromDateParameter
      Description: Defines the start date from which the mitigation is to be applied.
      Default value: Current date
      Mandatory: No
      
    - Name: toDateParameter
      Description: Sets the end date until which the mitigation is applicable.
      Default value: Calculated based on `fromDateParameter` + `mitigateDaysNum`
      Mandatory: No
      
    - Name: reasonParameter
      Description: Captures the reason for the SOD violation mitigation. Can be pre-filled from the last approval step's comments in the workflow or manually entered.
      Default value: N/A
      Mandatory: Yes
      
    - Name: approvedByParameter
      Description: Identifies who approved the mitigation process. Defaults to the user who performed the mitigation if not specified.
      Default value: User performing the action
      Mandatory: No
      
    - Name: doneByParameter
      Description: Indicates who is performing the mitigation action, usually the current user.
      Default value: Current user
      Mandatory: Yes
      
- Advanced:
    - Name: combinationName
      Description: The name of the violation combination to mitigate. This can directly target a specific SOD violation.
      Default value: N/A
      Mandatory: No
      
    - Name: controlParameter
      Description: Optional parameter for specifying a control relating to the mitigation.
      Default value: Same as reason if not provided
      Mandatory: No
      
    - Name: onlyExtendApprovedRisk
      Description: A Boolean flag to indicate whether to only extend the mitigation for already approved risks.
      Default value: false
      Mandatory: No

**Business impact:** This action directly impacts compliance and risk management processes within an organization by allowing for swift mitigation of identified SOD violations. By providing a structured and automated way to address these violations, it helps organizations maintain compliance with internal policies and regulatory requirements, minimizes potential access-related risks, and ensures continued operational integrity.

**Example of usage:** To mitigate a newly discovered SOD violation for a user, an administrator sets up the mitigation parameters including the `combinationName` of the violation, the `fromDateParameter` to start the mitigation, and the `mitigateDaysNum` to define the mitigation period. The action is executed to apply the necessary mitigations and document the process, with reasons and approvals recorded for audit purposes.

**Prerequisites:** Users executing this action must have appropriate permissions to manage SOD violations and access the information of users involved in the mitigation process. Additionally, a clear understanding of the SOD violation being addressed and the intended outcomes of the mitigation process is necessary to configure this action correctly.

**Error Handling and Troubleshooting:**

- Common Error: Mitigation already exists for user and combination
  - Cause: Trying to add mitigation for a combination where a mitigation already exists.
  - Solution: Check if the mitigation needs updating instead of creation, and use `onlyExtendApprovedRisk` as true if extending an existing mitigation.
  
- Common Error: AddMitigateToSodViolationForUser failed to validate for user and combination
  - Cause: Missing or invalid parameters, such as `userId`, `combinationId`, `reason`, `approvedBy`, `doneBy`, `fromDate`, `toDate`.
  - Solution: Ensure all mandatory parameters are provided and valid. Check if the dates are correctly formatted and future-dated as required.