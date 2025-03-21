# Hosting Server IISProcess

**Technical Name:** HostingServerIISProcess

**Category:** Configuration

**Default Value:** iisexpress.exe

**Impact Level:** Medium

**Description:**

The `HostingServerIISProcess` parameter specifies the default executable used by Pathlock's GRC platform to host web applications on Internet Information Services (IIS) Express. This setting is crucial for environments using IIS Express as their web server for hosting Pathlock applications.

**Business Impact:**

Configuring the correct IIS process ensures that the Pathlock GRC platform applications are hosted efficiently and securely. An incorrect setting may lead to inaccessibility or improper functioning of the Pathlock applications, affecting the organization's ability to manage security, risk, and compliance effectively.

**Technical Impact when configured:**

Proper configuration ensures that the Pathlock GRC platform's web applications are hosted using the intended web server process, leading to stable and secure access to the web applications. It impacts the application's performance, security, and compatibility with various web services.

**Examples Scenario:**

If a business decides to move from using a standard IIS server to IIS Express for development or lower environments, this parameter must be updated to ensure that the Pathlock application correctly interfaces with IIS Express. 

Scenario: An organization wants to create a development environment that closely mirrors their production but with fewer resources. They opt to use IIS Express instead of a full IIS setup. The `HostingServerIISProcess` parameter must be set to `iisexpress.exe` to facilitate this environment setup, ensuring smooth operation and testing of the Pathlock applications without the need for a full IIS server.

**Related Settings:** N/A

**Best Practices:** 

**Configure when:** Setting up or updating Pathlock GRC platform environments that utilize IIS Express for hosting applications, ensure that this parameter accurately reflects the executable name of the IIS Express process.

**Avoid when:** If your environment uses a full IIS server or a different web server solution, this parameter does not need to be configured as it pertains specifically to IIS Express setups.