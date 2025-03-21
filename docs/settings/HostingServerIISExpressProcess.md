# Hosting Server IISExpress Process

**Technical Name:** HostingServerIISExpressProcess 

**Category:** Configuration 

**Default Value:** 

**Impact Level:** Medium 

**Description:** This parameter controls the use of IIS Express for hosting services in a Pathlock Cloud GRC environment. Specifically, it determines whether IIS Express is utilized as the web server for deploying the Pathlock Cloud GRC platform, influencing how web services are hosted and managed within the system.

**Business Impact:** The selection between IIS Express and another web server infrastructure (like IIS Full) can significantly impact the deployment's scalability, security, and performance characteristics. Choosing IIS Express may benefit environments requiring lightweight, easy-to-configure hosting solutions, typically in development or testing scenarios.

**Technical Impact when configured:** Utilizing IIS Express affects the hosting environment's ability to scale and manage loads, potentially influencing the overall system performance. Besides, the choice of IIS Express may impose certain limitations on advanced configuration and security settings available through full IIS deployments.

**Examples Scenario:** In a development environment, where a team of Pathlock Cloud GRC platform developers requires a straightforward setup for testing new policies or configurations, opting for the HostingServerIISExpressProcess to utilize IIS Express can expedite the initial deployment and configuration phases, allowing for more immediate feedback and iteration.

**Related Settings:** 

**Best Practices:** configure when you are setting up a non-production environment that requires minimal setup and resources. Avoid when deploying a scalable, secure, and high-availability production environment that necessitates the full features of IIS.