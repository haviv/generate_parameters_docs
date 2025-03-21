**Technical Name:** WorkflowLocalizationByFieldId

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `WorkflowLocalizationByFieldId` parameter is designed to customize workflow forms by adjusting the title width based on specified CSS classes. This allows for dynamic layout adjustments within Pathlock GRC workflows, enabling better control over the user interface presentation according to business or regulatory requirements.

**Business Impact:**

Adjusting the form layout dynamically can enhance user experience, making workflows easier to navigate and understand. This can lead to improved efficiency in completing GRC tasks and ultimately support better compliance and risk management practices by ensuring that important information is clearly visible and accessible.

**Technical Impact: when configured**

When the `WorkflowLocalizationByFieldId` parameter is configured, it dynamically adjusts the width of titles in workflow forms based on the associated CSS classes. This can impact how information is presented to the user, potentially improving clarity and accessibility of form fields and controls in workflows.

**Examples Scenario:**

A workflow in the Pathlock GRC platform requires the display of a form with various sections that need distinct visual emphasis. By configuring this parameter, sections of the form can be visually adjusted without the need for hard coding these changes, thus allowing for a flexible adaptation to specific workflow requirements.

**Related Settings:** 

- `RequestsWaitingForApprovalGetDataFromStoredProcedure`
- `AuthorizationReviewForSoDActivityDrillDown`

**Best Practices:** configure when

- Dynamic layout adjustments are necessary for specific workflows to enhance user understanding or interaction.
- There is a need to comply with detailed presentation requirements specified in internal guidelines or regulatory standards.

avoid when

- The default layout settings meet the workflow requirements, and no significant improvement in user interaction is anticipated from layout adjustments.
- The complexity of layout adjustments could potentially confuse users or detract from the primary objectives of the workflow.