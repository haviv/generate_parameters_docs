**External Dlls Folder**

**Technical Name:** ExternalDllsFolder

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The ExternalDllsFolder parameter specifies the directory path used by Pathlock GRC platform components to store and access external dynamic link libraries (DLLs). This setting plays a crucial role in extending the functionality and customizing the behavior of various modules within the application, such as connectors, report customization, and service processing.

**Business Impact:**

Proper configuration of the ExternalDllsFolder can significantly enhance the platform's flexibility in integrating with external systems, generating customized reports, and improving service responsiveness. It allows for a more tailored operational experience, impacting the efficiency of risk, compliance, and security management workflows.

**Technical Impact when configured:**

When configured, the ExternalDllsFolder allows for dynamic loading of external libraries at runtime, affecting how the application interacts with components like SharePoint sites, Office Online connectors, and custom report generation. It is essential for ensuring that additional functionalities provided by external DLLs are accessible and properly executed by the platform.

**Examples Scenario:**

- SharePoint Integration: Custom connectors utilizing external DLLs for enhanced data processing and integration with SharePoint Online.
- Custom Report Generation: Enabling advanced report customization features by accessing specific DLLs for report generation and customization processes.
- Service Extensions: Providing additional services or enhancing existing ones by dynamically loading external libraries as needed for various background services and web collectors.

**Related Settings:** N/A

**Best Practices:** 

- **Configure when:**
  - Extending the platform's capabilities with custom-developed functionalities that require external DLLs.
  - Integrating with third-party systems or services that demand specific libraries not included with the standard installation.
- **Avoid when:**
  - There is insufficient knowledge about the security and stability of the external libraries being incorporated.
  - The platform’s default functionalities meet the organization's needs without additional customizations.