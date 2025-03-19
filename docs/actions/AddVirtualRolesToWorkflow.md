# Add Virtual Roles to Workflow

**Category:** Workflow

**Description:**
The "Add Virtual Roles to Workflow" action is designed to automate the process of adding virtual roles to a workflow within the Pathlock Cloud platform. This action dynamically creates virtual roles based on specified attributes and associates these roles with SAP systems. It allows for flexibility in handling role assignments by using a collection-based approach, accommodating both single attribute modes (where virtual roles are created for each attribute-value pair) and multiple attribute modes. The workflow parses input parameters to shape the collection of roles and attributes, applying custom value separators and translating technical names to human-readable names where necessary. In essence, this action streamlines the process of role management in identity governance scenarios, making it easier to manage access rights and permissions.

**Parameters:**

- **Basic Parameters:**
    - Name: AddVirtualRolesToWorkflow_CollectionName
      Description: The name of the collection to be used for generating virtual roles. It identifies which collection within the workflow's context should be processed to create virtual roles.
      Default value: None
      Mandatory: No
      
    - Name: AddVirtualRolesToWorkflow_RoleNameField
      Description: Specifies the field name within the collection that holds the role name. This parameter is critical for identifying how roles are named in the resulting virtual roles.
      Default value: "RoleName"
      Mandatory: No

- **Advanced Parameters:**
    - Name: AddVirtualRolesToWorkflow_CustomValueSeparator
      Description: Custom separator used for parsing attribute values. It supports customizing how multi-valued attributes are split into individual values.
      Default value: ",", "\n"
      Mandatory: No

    - Name: AddVirtualRolesToWorkflow_SingleAttributeMode
      Description: Determines if the virtual roles should be created for each attribute-value pair (true), or as a combined set of attributes (false).
      Default value: false
      Mandatory: No

    - Name: AddVirtualRolesToWorkflow_templateFunctionToMapAttributeName
      Description: Mapping function for translating technical attribute names to user-friendly names, specified in a key=value format. This affects how attribute names are presented in virtual roles.
      Default value: None
      Mandatory: No

    - Name: AddVirtualRolesToWorkflow_Attributes
      Description: Specifies the technical names for attributes (CSV format), which are considered when creating virtual roles. Relevant only when defining attributes that inform the virtual role creation.
      Default value: "Attributes"
      Mandatory: No

**Business impact:**
Implementing the Add Virtual Roles to Workflow action within Pathlock Cloud enhances the efficiency and accuracy of role management processes. Specifically, it aids in the dynamic creation and assignment of roles, catering to complex identity and access management requirements in an automated manner. This results in significant time savings and reduces the likelihood of human errors in role assignments, ultimately strengthening governance, risk, and compliance (GRC) frameworks.

**Example of usage:**
Imagine a scenario where an organization requires the creation of virtual roles based on specific attributes within a user access request for an SAP system. By setting up this action, the system admin specifies the collection name, the role name field, and attributes of interest. The action then processes this data, creating virtual roles for each attribute specified or grouping them as defined, and updates the workflow with these roles, ready for further processing such as approval or provisioning.

**Prerequisites:**
- Administrator access to Pathlock Cloud is required to configure this action.
- Understanding of the existing collections and their attributes within the workflow system.
- SAP System IDs should be known and accessible by the action for role-grouping purposes.

**Error Handling and Troubleshooting:**
- **Problem:** No virtual roles are created.
  - **Cause:** RoleName field might be incorrectly specified, or the collection does not exist.
  - **Solution:** Verify the collection name and RoleName field accuracy. Ensure that they match exactly with what is available in the workflow context.

- **Problem:** Incorrect virtual roles are created.
  - **Cause:** Attribute mappings or value separators might be incorrectly configured.
  - **Solution:** Review the template function for attribute name mapping and the custom value separator. Adjust them as necessary to match the expected input format.

- **Problem:** Duplicate virtual roles are created.
  - **Cause:** Roles are not being correctly grouped by their unique identifiers.
  - **Solution:** Ensure that the virtual roles are properly deduplicated by reviewing the grouping logic, particularly the implementation around `resultRoles.GroupBy(x => x.RoleId)`.