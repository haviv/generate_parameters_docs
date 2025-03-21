**Process Control Action Configuration**

**Technical Name:** ProcessControlActionConfiguration

**Category:** Configuration

**Default Value:** True

**Impact Level:** Medium

**Description:**

The Process Control Action Configuration parameter enables or disables the execution of processes related to organization structure synchronization in cloud environments. When set to true, it allows these processes to run in the cloud, thereby ensuring that the organizational hierarchy is current and accurately reflected in Pathlock's GRC platform.

**Business Impact:**

Setting this parameter to true enhances the platform's ability to manage security, risk, and compliance by ensuring that any changes in the organization's structure are promptly and accurately reflected. This real-time update can impact access controls, risk assessments, and compliance reporting by making sure they are all aligned with the current organizational structure. 

**Technical Impact when configured:**

When configured to true, it allows the Pathlock GRC platform to automatically synchronize and update the organizational structure from cloud-based sources. This ensures that the platform’s security, risk, and compliance functions are always operating with the most current data.

**Examples Scenario:**

A company reorganizes its departments and updates its organization structure in a cloud-based HR system. With ProcessControlActionConfiguration set to true, Pathlock’s GRC platform can automatically fetch and apply these updates, ensuring that risk and compliance assessments are conducted based on the latest organizational structure, thereby maintaining accurate and current compliance and risk management posture.

**Related Settings:**

- `RestOrganizationStructureProvider_RunInCloud`

**Best Practices:** configure when the organizational structure is managed or frequently updated in the cloud, avoid when the organization structure is static or managed locally to prevent unnecessary synchronization actions.