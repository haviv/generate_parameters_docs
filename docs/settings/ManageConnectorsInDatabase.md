# Manage Connectors In Database

**Technical Name:** ManageConnectorsInDatabase

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls the inclusion and setup of various system connectors within the database. It specifically enables the configuration of connectors for different ERP systems by tailoring them to match specific database requirements and system mappings.

**Business Impact:**

Proper management of connectors is crucial for the seamless integration of Pathlock GRC with an organization's ERP systems. This ensures that security, compliance, and risk management processes are accurately extended across all connected platforms, offering a unified approach to GRC management.

**Technical Impact when configured:**

- Ensures compatibility between Pathlock GRC platform and the ERP systems.
- Facilitates accurate data exchange and reporting by aligning system connectors with database specifications.
- Supports tailored configurations for different ERP systems, enhancing system-specific compliance and monitoring capabilities.

**Examples Scenario:**

A company uses PeopleSoft for HR management and SAP for finance operations. By configuring the `ManageConnectorsInDatabase` parameter, the organization can ensure that the Pathlock GRC platform accurately interacts with both PeopleSoft and SAP systems, reflecting the correct data and compliance checks in the GRC reports.

**Related Settings:**

- WorkflowUploadForbiddenFileTypes

**Best Practices:** 

- **Configure when:** Setting up the Pathlock platform for the first time or adding new ERP systems to the platform.
  
- **Avoid when:** The existing configurations adequately support all connected ERP systems, and no new systems are being added.