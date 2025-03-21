# Snc Partner Name

**Technical Name:** SncPartnerName

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** The SncPartnerName parameter is used to specify the partner name for Secure Network Communications (SNC) within the connection configuration to an SAP system. This parameter is crucial for enabling secure communications by establishing trust relationships between different parties in the network.

**Business Impact:** Setting the SncPartnerName correctly ensures that sensitive data transmitted between the Pathlock GRC platform and the SAP system is encrypted, thereby reducing the risk of data breaches and enhancing compliance with data protection regulations.

**Technical Impact when configured:** When the SncPartnerName is properly configured, it activates SNC protection for the connections, ensuring all data traffic between systems is encrypted. This configuration helps in protecting against eavesdropping and tampering by unauthorized parties.

**Examples Scenario:** An organization wants to ensure that all communications between their Pathlock GRC platform and SAP systems are secure to protect financial data and personally identifiable information (PII). By configuring the SncPartnerName with the correct partner name, they can enable SNC, thereby encrypting all data in transit.

**Related Settings:** RfcConfigParameters.AppServerHost, RfcConfigParameters.MessageServerService, RfcConfigParameters.LogonGroup, RfcConfigParameters.SystemID

**Best Practices:** configure when setting up secure communications between Pathlock GRC and SAP systems; avoid when there's no requirement for SNC in the system landscape.