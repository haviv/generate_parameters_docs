**Application base URL:** 

**Technical Name:** SiteAddress 

**Category:** Configuration 

**Default Value:** [empty] 

**Impact Level:** High 

**Description:** 

The SiteAddress parameter specifies the base URL of the application. This setting is crucial for ensuring that generated reports and various platform functionalities correctly reference the underlying framework and resources of the Pathlock Cloud GRC platform. 

**Business Impact:** 

Configuring the SiteAddress correctly ensures seamless integration of report generation, user interface elements, and navigation within the Pathlock GRC platform. It directly affects the accessibility and operability of the platform for end users by enabling accurate redirection and resource loading.

**Technical Impact when configured:** 

- Enables the generation of reports with correct URLs pointing back to the application.
- Facilitates accurate redirect operations and seamless navigation within the platform.
- Ensures that popup pages and other platform components load with the appropriate styles and user interface elements.

**Examples Scenario:** 

If your Pathlock Cloud GRC platform is hosted at `https://grc.mycompany.com`, setting the SiteAddress to this URL ensures that all generated reports, links within emails, and navigational components within the platform correctly use this base URL.

**Related Settings:** 

- ReportExportTester AppConfiguration: For setting up environment-specific parameters including the SiteAddress.
- ProfileTailor Reports Infrastructure: Uses the SiteAddress for correct stylesheet theme application in report pages.

**Best Practices:** 

- Configure the SiteAddress as soon as the Pathlock GRC platform setup is completed, and before deploying it to end users.
- Avoid changing the SiteAddress frequently to prevent disruption in platform accessibility and functionality.