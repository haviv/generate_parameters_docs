# Show Default Text For Empty Workflow Form Fields

**Technical Name:** ShowDefaultTextForEmptyWorkflowFormFields

**Category:** Configuration

**Default Value:**

**Impact Level:** Low

**Description:**

This parameter controls the display behavior for empty fields within workflow forms. When enabled, specific default text is shown in empty fields of the workflow form, enhancing user understanding and guiding them towards completing the form correctly.

**Business Impact:**

Improving the user interface by displaying default text in empty workflow form fields can lead to better guidance and fewer errors during form completion. This can indirectly improve the efficiency and effectiveness of business processes managed through the Pathlock platform.

**Technical Impact when configured:**

When activated, this setting affects how empty fields are displayed to the user in workflow forms. It ensures that users are guided with predefined text, potentially reducing confusion and mistakes during data entry.

**Examples Scenario:**

- **Before Activation:** An empty workflow form field might confuse users, leading to skipped entries or queries to administrators.
- **After Activation:** Empty fields display a default text such as "Please enter value," guiding users to complete the form without additional instructions.

**Related Settings:**

- **ElementsIdsToHideOnPreview:** Defines elements to be hidden on the workflow form preview, working in tandem with showing default texts in others.

**Best Practices:** 

- **Configure when:** You have identified specific workflow forms where users frequently encounter confusion due to empty fields.
- **Avoid when:** Every field in your workflow forms is self-explanatory, or additional default text could cause confusion.