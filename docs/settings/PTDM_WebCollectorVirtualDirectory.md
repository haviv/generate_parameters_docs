# PTDM Web Collector Virtual Directory

**Technical Name:** PTDM_WebCollectorVirtualDirectory

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The PTDM Web Collector Virtual Directory parameter specifies the virtual directory path used by the Pathlock platform for the web-based data collection. This setting is crucial for correctly routing and securing web-collected data within the Pathlock environment.

**Business Impact:**

Proper configuration of this parameter ensures that data collected through web interfaces is handled securely and efficiently, contributing to the overall integrity and compliance of the organization's GRC (Governance, Risk Management, and Compliance) processes.

**Technical Impact when configured:**

When correctly configured, the PTDM Web Collector Virtual Directory securely directs collected data to the specified location, facilitating accurate and secure data processing. Misconfiguration of this parameter can lead to data routing issues, impacting the integrity of the data collection process and potentially leading to data loss or exposure.

**Examples Scenario:**

An organization needs to collect audit trail information from web interfaces securely. By setting the PTDM Web Collector Virtual Directory to a controlled, secure path, the organization ensures that this sensitive information is correctly routed through the Pathlock platform, enhancing data security and compliance with internal and regulatory standards.

**Related Settings:**

- `ApplicationVirtualDirectory`

**Best Practices:** 

- **configure when** setting up or reconfiguring web-based data collection pathways to ensure secure and accurate data routing.
- **avoid when** there is no clear requirement for web-based data collection or when alternative data collection methods are more appropriate.