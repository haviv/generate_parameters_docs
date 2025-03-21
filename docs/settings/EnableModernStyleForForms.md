# Enable Modern Style For Forms

**Technical Name:** EnableModernStyleForForms

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter controls the injection of modern styling into forms within the Pathlock GRC platform. Enabling this feature modernizes the appearance of user interfaces, enhancing the visual experience and usability for the end-user.

**Business Impact:** Enabling modern styling for forms can significantly improve the user experience by providing a more contemporary and visually appealing interface. This can lead to improved user engagement and productivity, as well as potentially reducing training time for new users unfamiliar with older interface styles.

**Technical Impact when configured:** When enabled, this setting applies modern CSS and JavaScript enhancements to forms, overriding default styling options. This change is dynamic and does not require modifications to underlying form templates or structure.

**Examples Scenario:** A company has been using the Pathlock GRC platform for several years and is looking to update its interface without major system overhauls. By enabling the `EnableModernStyleForForms` parameter, they can instantly modernize the look and feel of their forms, making them more visually appealing and user-friendly.

**Related Settings:**
- `ModernUIShowWorkflowsMenu`

**Best Practices:** 
- **Configure when:** You wish to enhance the visual appearance and user experience of your GRC platform without extensive custom development.
- **Avoid when:** Users are accustomed to the existing interface, and a sudden change could disrupt their workflow or when compatibility issues with custom styling or scripts are a concern.