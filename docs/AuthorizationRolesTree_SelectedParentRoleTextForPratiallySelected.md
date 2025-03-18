# Authorization Roles Tree Selected Parent Role Text For Partially Selected

**Technical Name:** AuthorizationRolesTree_SelectedParentRoleTextForPratiallySelected

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter is used to customize the text representation of parent roles within the authorization roles tree that are partially selected in the Pathlock Cloud GRC platform.

**Business Impact:** Proper configuration of this parameter enhances user experience by providing clear visual feedback on the selection state of parent roles in complex hierarchical structures. It streamlines role selection processes during workflows such as risk assessment or access reviews, thereby reducing the risk of oversight or errors.

**Technical Impact when configured:** When set, this parameter affects how parent roles that are not fully selected (i.e., only some of their child roles are selected) are displayed in the user interface, particularly in workflows that involve the manipulation of role-based access controls.

**Example Scenario:** In a scenario where a user is assigning access roles to a new employee, the system might display each partially selected parent role in a distinct manner (as defined by this parameter) to indicate that the user has not assigned all possible permissions under that role. This feedback can prompt the user to review and possibly revise the permissions being granted.

**Related Settings:** 
- AuthorizationRolesTree_SelectedParentRoleTextForFullySelected

**Applicable Workflows Actions:** 

**Best Practices:** 
- **Configure when**: You need to improve clarity in the display of role hierarchies where only partial selections are common.
- **Avoid when**: The default display configuration aligns with user expectations in your organizational context.