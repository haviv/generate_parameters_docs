# PTDM IISApp Root Path

**Technical Name:** PTDM_IISAppRootPath

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The PTDM_IISAppRootPath parameter specifies the root directory path for Internet Information Services (IIS) applications within the Pathlock Cloud GRC platform. This setting is crucial for defining where the application's files and resources are located on the server.

**Business Impact:**

Correct configuration of this parameter ensures that the GRC application operates seamlessly, accessing the necessary files and resources efficiently. Misconfiguration may lead to issues in application functionality, impacting compliance reporting, risk management, and security policy enforcement activities.

**Technical Impact when configured:**

When configured correctly, the PTDM_IISAppRootPath parameter allows the GRC platform to locate and access application files, supporting the smooth operation of the platform’s security, risk, and compliance features. Incorrect paths can result in runtime errors, inaccessible resources, or failure in application deployment.

**Example Scenario:**

A financial institution uses the Pathlock Cloud GRC platform to manage its compliance with financial regulations. Correctly setting the PTDM_IISAppRootPath ensures that all compliance reports, risk assessment tools, and policy management functionalities are accessible and operate without interruptions, thereby maintaining the institution's regulatory compliance status.

**Related Settings:**

- CommonSettings.Default.LoginMethod

**Best Practices:** 

- **Configure when:** Setting up the Pathlock Cloud GRC platform for the first time or moving the application to a new server environment.
- **Avoid when:** The specified directory path does not exist or the application server does not have the appropriate permissions to access the directory.