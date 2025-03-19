# Authorization Roles Tree Selected Parent Role Text For Fully Selected

**Technical Name:** AuthorizationRolesTree_SelectedParentRoleTextForFullySelected

**Category:** Configuration

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter is used within the Pathlock Cloud GRC platform to represent the textual description for a parent role that has all its child roles selected. It is primarily employed in the context of optimizing and streamlining the user interface related to authorization roles management and workflows like the removal of roles from elements. This setting essentially helps in differentiating between fully selected parent roles and those that are not, by providing a specific text label for fully selected ones.

**Business Impact:**

Proper configuration of this parameter will enhance the user experience by offering clear and straightforward visuals and descriptions of roles hierarchies. It aids administrators in swiftly comprehending the structure and state of roles' selections, which can lead to more efficient decision-making in terms of user access and permissions management.

**Technical Impact when configured:**

When configured, this parameter influences how parent roles are rendered in the user interface when all their respective child roles are selected. It serves as an indicator, simplifying the visual representation and management of complex roles structures within the organization.

**Example Scenario:**

Consider a scenario where an organization has implemented a structured set of roles within their GRC platform, including parent roles with numerous child roles beneath them. Setting a clear descriptor for fully selected parent roles allows administrators or auditors to quickly identify and understand the extent of permissions granted by those parent roles without having to manually check each child role.

**Related Settings:** 

- EveryoneRoleInPTD

**Applicable Workflows Actions:**

- RemoveRolesListElementExcludeRolesFromOtherElement

**Best Practices:** 

- Configure when: You have a complex role structure with many layers of parent and child roles, and you want to streamline the roles management process.
- Avoid when: The role structure is straightforward with minimal nested roles, or if distinguishing between fully selected parent roles and others is not necessary for your organization's GRC processes.