# PTDM App Virtual Directory

**Technical Name:** PTDM_AppVirtualDirectory

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `PTDM_AppVirtualDirectory` parameter specifies the virtual directory path for the application within the Pathlock Cloud GRC platform. This path is critical for the application to correctly locate and serve resources such as logos and other customized elements.

**Business Impact:**

Configuring the `PTDM_AppVirtualDirectory` correctly ensures that the application can efficiently locate and serve necessary resources. It directly impacts the user interface by determining how and from where the application loads resources, which can affect loading times, resource availability, and overall user experience.

**Technical Impact when configured:**

- Ensures seamless access to application resources.
- Improves load times for resources stored within the specified directory.
- Enables the customization of application elements such as logos.

**Example Scenario:**

- An administrator needs to update the corporate logo across the Pathlock Cloud GRC platform. By correctly configuring the `PTDM_AppVirtualDirectory`, the system knows exactly where to retrieve the new logo file from, ensuring the update is reflected across the platform.

**Related Settings:**

- WebCollectorVirtualDirectory

**Best Practices:** 

- **Configure when:** setting up or migrating the Pathlock Cloud GRC platform to a new server or when organizational resources like logos and custom UI elements are updated or relocated.
  
- **Avoid when:** the default configuration meets your organization's requirements, or if changes might conflict with predefined resource paths critical for the application's operation.