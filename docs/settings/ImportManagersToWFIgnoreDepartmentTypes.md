# Ignore These Organization Unit Types

**Technical Name:** ImportManagersToWFIgnoreDepartmentTypes

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter allows for the exclusion of specific organizational unit types during the import process of managers into workflows. It is used to fine-tune the entities included in the automation processes by identifying and ignoring designated department types to streamline compliance and security protocols.

**Business Impact:**

Setting this parameter correctly ensures that only the relevant organizational units are considered in workflow processes, thereby improving the efficiency of compliance and security operations within the organization. It helps in avoiding unnecessary processing of unrelated or unimportant department types, leading to more focused and accurate compliance and risk management efforts.

**Technical Impact when configured:**

When configured, this parameter filters out the specified organizational unit types from being considered in the group generation process for workflows. This streamlines the operations by focusing only on pertinent departments, thus optimizing the performance and accuracy of security, risk, and compliance activities.

**Examples Scenario:**

If the organization wants to exclude temporary or seasonal departments from being part of certain compliance processes, setting this parameter with the appropriate department types as values will automatically filter them out from the workflow's scope.

**Related Settings:**

- `ImportDefinition.UserGroupTypeId`

**Best Practices:** configure when the workflow process should be optimized by excluding irrelevant department types. Avoid when all organizational units are relevant to the workflow processes being executed.