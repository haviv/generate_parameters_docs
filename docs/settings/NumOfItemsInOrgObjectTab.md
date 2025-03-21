# Num Of Items In Org Object Tab

**Technical Name:** NumOfItemsInOrgObjectTab

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The parameter 'NumOfItemsInOrgObjectTab' controls the display limit for items within the Organization Object Tab in the Pathlock Cloud GRC platform. It is designed to improve user interface efficiency and manage system performance by limiting the number of displayed items.

**Business Impact:**

Choosing an optimal value for this parameter can enhance the user experience by preventing information overload and ensuring that the application performs optimally, even when handling a large set of organizational objects. It directly impacts how users interact with and manage security, risk, and compliance data related to organizational objects.

**Technical Impact when configured:**

When configured, this parameter directly affects the system's data retrieval and display mechanisms, potentially improving application responsiveness and user satisfaction by streamlining the amount of data loaded on the screen at any one time.

**Examples Scenario:**

For example, if the 'NumOfItemsInOrgObjectTab' is set to 50, when a user navigates to the Organization Object Tab, only the first 50 items (e.g., user roles, permissions, etc.) will be displayed. This limit helps in managing the system's performance and improves user experience on platforms with a large number of organizational objects to manage.

**Related Settings:**

- NotAllowedChractersUploadFile
- NoDaysGoBackFor

**Best Practices:** configure when the number of organizational objects is significantly large to ensure optimal performance and a good user experience, avoid when the organizational scope is small to ensure comprehensive visibility.