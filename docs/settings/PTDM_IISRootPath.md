# PTDM IISRoot Path

**Technical Name:** PTDM_IISRootPath

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The PTDM_IISRootPath parameter specifies the root file path for the IIS (Internet Information Services) configuration in the Pathlock cloud GRC platform. This path is essential for locating and managing web application files and assets across the platform.

**Business Impact:**

Determining the correct root path for IIS is critical for ensuring that web applications and services within the Pathlock platform are correctly served and managed. An incorrectly configured IIS root path could lead to disruptions in service availability, impacting user access and functionality within the GRC platform.

**Technical Impact when configured:**

Correctly configuring the PTDM_IISRootPath ensures that the Pathlock platform's web services and applications are properly located and accessible by the system. This configuration is vital for the seamless operation and integration of various Pathlock components and external services, ensuring that security, risk, and compliance functions are efficiently managed and executed.

**Examples Scenario:**

For instance, after a system upgrade or migration, the IIS root path might change. Updating the PTDM_IISRootPath parameter accordingly will ensure that all web applications and services are correctly pointed to the new location, preventing any downtime or accessibility issues for end-users.

**Related Settings:**

- `LoaderPath` in the System Registry for DataFlower service
- `LogoHtmlFilePath` for the location of custom logo HTML files

**Best Practices:** 

- **configure when:** setting up the Pathlock platform for the first time or moving web applications to a new server or directory.
- **avoid when:** the current configuration is correctly pointing to the IIS root path where all necessary files and applications are stored and accessible.