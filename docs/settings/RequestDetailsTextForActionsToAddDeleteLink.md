**Request Details Text For Actions To Add Delete Link**

**Technical Name:** RequestDetailsTextForActionsToAddDeleteLink

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:** This parameter customizes the text displayed for actions related to adding or deleting links within the workflow user interface (UI) and workflow emails. It allows for clearer communication regarding the intention and effect of workflow actions, particularly in contexts where actions to add or delete links are executed.

**Business Impact:** Proper configuration of this parameter ensures that users and approvers within the workflow understand the significance and implications of add or delete actions, leading to informed decision-making and a smoother workflow process. Misinterpretation of these actions can lead to unintended access changes or workflow disruptions, directly impacting security and compliance postures.

**Technical Impact when configured:** Enhances user experience by providing explicit text descriptions for add or delete link actions within workflows, reducing confusion and potential errors. It may also aid in audit trails by clearly delineating the intent of each action in a comprehensible format.

**Examples Scenario:** When a user requests access to a new resource, the workflow might include an action to link the user's account to the resource. With `RequestDetailsTextForActionsToAddDeleteLink` properly configured, the approval email can clearly state, "Approve to add access link for User X to Resource Y," making the approval decision easier and clearer for the approver.

**Related Settings:**

- `RequestApproved`
- `RequestApprovedTemplateId`

**Applicable Workflows Actions:** 

**Best Practices:** 

- **Configure when:** Setting up workflows that include actions to modify user access or resource links. Clear, descriptive text helps avoid misinterpretation.
- **Avoid when:** The workflow actions are self-explanatory and do not benefit from additional clarification.