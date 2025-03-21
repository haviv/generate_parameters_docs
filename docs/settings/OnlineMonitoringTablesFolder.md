# Online Monitoring Tables Folder

**Technical Name:** OnlineMonitoringTablesFolder

**Category:** Configuration

**Default Value:** N/A

**Impact Level:** High

**Description:**
The Online Monitoring Tables Folder parameter specifies the directory where the online monitoring system's tables are stored. This directory is used by the Pathlock GRC platform to read and analyze data for authorization review, compliance checks, and other security and risk management processes.

**Business Impact:**
Proper configuration of this parameter is crucial for the effective monitoring and analysis of authorization and access controls within the organization's systems. It supports compliance with internal and external audit requirements by ensuring that access rights are appropriately managed and reviewed.

**Technical Impact when configured:**
- Enables the Pathlock platform to accurately locate and process the necessary tables for online monitoring tasks.
- Improves the efficiency of data analysis for authorization reviews and compliance assessments.
- Ensures the reliability of the data used for security and risk management decisions.

**Examples Scenario:** An organization implements the Pathlock GRC platform to enhance their security and compliance posture. By correctly setting the Online Monitoring Tables Folder, the organization ensures that the platform can seamlessly access and analyze the necessary data to monitor user authorizations across SAP and SQL databases, thereby identifying potential SoD (Segregation of Duties) conflicts and unauthorized access risks.

**Related Settings:**
- ActiveDirectoryDirectoryMonitoringIgnoredPatterns
- AddWebDynprosToTransactions

**Best Practices:** 
- **Configure when:** Setting up Pathlock for the first time or when the location of online monitoring tables changes due to system updates or migration.
- **Avoid when:** The specified folder does not have the necessary permissions or contains irrelevant data that could lead to incorrect analysis or system performance issues.