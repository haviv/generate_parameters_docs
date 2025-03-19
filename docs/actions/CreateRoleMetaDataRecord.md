# CreateRoleMetaDataRecord

**Category:** User Management

**Description:**

The `CreateRoleMetaDataRecord` action is a key component of the Pathlock Cloud's workflow engine, specifically designed to streamline the identity and access management processes. This action is tasked with creating or updating metadata for roles within the system. It commences by checking the existence of the role by its name. If the role doesn't exist, a new metadata record is created; otherwise, the existing record is updated. 

This action allows setting various attributes of a role such as system group, category, business unit, risk level, business process, and a range of up to ten customizable metadata attributes. It also handles the designation of a role as a business role and allows for marking the role as read-only. The culmination of this process includes updating related records, ensuring the new or updated role metadata is correctly associated with system roles or business roles as necessary.

**Parameters:**

- Basic:
    - Name: NewRoleName
    - Description: The name of the role to create or update metadata for. Used as a key to check whether the metadata for a role already exists and acts as a primary identifier for the role.
    - Default value: None
    - Mandatory: yes
    
    - Name: CreateBusinessRoleWorkflow
    - Description: A boolean parameter that specifies whether the role being created or updated is a business role.
    - Default value: false
    - Mandatory: no

- Advanced:
    - Name: MetaRoleSystemGroup
    - Description: Associates the role with a specific system group by its name. Relevant for system-based role categorization.
    - Default value: None
    - Mandatory: no

    (Additional parameters such as MetaRoleCategory, MetaRoleBusinessUnit, MetaRoleRiskLevel, MetaRoleBuisnessProcess, MetaRoleIsReadOnly, MetaRoleBusinessNeed, MetaRoleLongDescription, and MetaDataRoleAttribute1 through MetaDataRoleAttribute10 follow a similar format, specifying various attributes of the role metadata.)

**Business Impact:**

Implementing the `CreateRoleMetaDataRecord` action significantly improves the efficiency of managing roles within the Pathlock Cloud platform. It automates the otherwise manual and time-consuming process of creating and updating role metadata, ensuring that access management is both accurate and reflects current business needs. By enabling precise configuration of role attributes, it supports adherence to security policies, compliance requirements, and risk management strategies.

**Example of Usage:**

To create or update a role named "FinancialManager" with a specific risk level and business unit:

1. Set `NewRoleName` to "FinancialManager".
2. Optionally set `CreateBusinessRoleWorkflow` to true if it is a business role.
3. Provide values for parameters such as `MetaRoleRiskLevel` and `MetaRoleBusinessUnit` to categorize the role accordingly.
4. Execute the action to create or update the role's metadata within Pathlock Cloud.

**Prerequisites:**

- Necessary permissions to manage roles and their metadata within the Pathlock Cloud platform.
- Understanding of the existing role categories, risk levels, and other attributes within the organization's implementation of Pathlock Cloud.

**Error Handling and Troubleshooting:**

- **Missing NewRoleName Parameter:** If the `NewRoleName` parameter is not provided, the action will fail with a message indicating that the NewRoleName is missing. Ensure this parameter is correctly specified.
- **Invalid Parameter Values:** If non-existent names are used for system groups, role categories, or other attributes, the record may be created with incomplete information. Verify the existence of these entities within the Pathlock Cloud before executing the action.
- **Permission Errors:** Ensure the executing account has appropriate permissions to create and modify role metadata in the system. If errors persist, contact system administration for access review.