# PDTM Web Collector Virtual Directory

**Technical Name:** PDTM_WebCollectorVirtualDirectory

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:** The PDTM Web Collector Virtual Directory parameter is used to specify the virtual directory path for the web collector within the Pathlock GRC platform. This setting is crucial for ensuring that the collected data via web interfaces is securely and efficiently directed to the designated storage location within the platform's infrastructure.

**Business Impact:** Correct configuration of this parameter ensures the seamless collection and processing of data from web sources, facilitating continuous monitoring and alerting on security, risk, and compliance events. Misconfiguration could lead to data collection disruptions, impacting the organization's ability to respond to threats and compliance requirements in a timely manner.

**Technical Impact when configured:** Properly setting the PDTM Web Collector Virtual Directory enhances the platform's data collection capabilities, ensuring reliability and security. It directly affects the efficiency of event and alert configurations within the system.

**Examples Scenario:** An organization needs to adjust the destination folder for web-collected data due to a change in their IT infrastructure. By configuring the PDTM Web Collector Virtual Directory parameter, they ensure that data from web sources continues to be collected without interruption, maintaining their security and compliance posture.

**Related Settings:** 

**Best Practices:** 

- **Configure when:** setting up or updating the Pathlock GRC platform to ensure that the web collector data is correctly targeted to the designated virtual directory.
  
- **Avoid when:** the default settings align with the organization's current infrastructure and no changes in the web collector's data path are necessary.