# Portal - Show navigation path

**Technical Name:** Portal_ShowBreadCrumb

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**
The `Portal_ShowBreadCrumb` parameter controls the visibility of the navigation path (commonly known as breadcrumbs) on the Pathlock Cloud GRC platform. When enabled, it displays a hierarchical navigation path, helping users understand their current location within the platform and navigate quickly to parent sections or categories.

**Business Impact:**
Enabling breadcrumbs improves user navigation and overall user experience by providing clear pathways back to higher-level pages. It is particularly beneficial for new users or large organizations with complex GRC structures, as it aids in the efficient exploration and use of the Pathlock platform, potentially reducing training time and increasing productivity.

**Technical Impact when configured:**
- **Enabled:** Displays a breadcrumb trail for users, enhancing navigability and understanding of the platform structure.
- **Disabled:** Breadcrumbs are not shown, which may simplify the interface but at the cost of potentially making navigation more challenging for users.

**Examples Scenario:**
- A new compliance officer needs to review various reports and settings deep within the Pathlock platform. With breadcrumbs enabled, they can easily navigate to parent categories or quickly return to the homepage without multiple clicks or getting lost.
  
**Related Settings:**
- `Portal_ItemFontSize`
- `Portal_ItemFontName`

**Best Practices:** 
- **Configure when:** Navigational clarity and user experience are a priority for your organization, especially in complex settings with multiple layers of navigation.
- **Avoid when:** Minimalism is preferred in the user interface, and users are already familiar with the platform structure or when screen real estate is at a premium.