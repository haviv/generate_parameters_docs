# Fiori Connector Identify Based On Catalogs

**Technical Name:** FioriConnectorIdentifyBasedOnCatalogs

**Category:** User Management

**Default Value:** True

**Impact Level:** High

**Description:**

The Fiori Connector Identify Based On Catalogs parameter is used to configure the identification of SAP Fiori usage based on the catalogs. This setting enables the SAP Fiori connector to read Fiori OData catalogs to map services to applications, thereby identifying which Fiori applications are being used.

**Business Impact:**

Enabling this parameter ensures accurate tracking and management of user access and activities within SAP Fiori applications. It supports compliance with internal and external audit requirements by providing transparent and controlled access to Fiori apps. This contributes to improved security and governance in the Fiori landscape.

**Technical Impact when configured:**

When configured, this feature activates the FioriODataCatalogReader, allowing the Pathlock Cloud GRC platform to accurately identify and track usage of Fiori applications. This helps in the detailed analysis of roles, authentification objects, and app usage, significantly enhancing visibility and control over the security within SAP Fiori.

**Examples Scenario:**

- An organization needs to comply with audit requirements by providing detailed logs of user access and activities within their SAP Fiori environment. By having FioriConnectorIdentifyBasedOnCatalogs enabled, they can ensure that all user interactions with Fiori applications are accurately recorded and easily auditable.

**Related Settings:**

- AuthorizationCertificationByActivitiesIncludeRoleName

**Best Practices:** 

- **Configure when:** You have a complex Fiori landscape and need precise control and visibility over user access and activities within Fiori apps.
- **Avoid when:** Your organization does not use SAP Fiori, or there is no requirement for detailed tracking of Fiori application usage.
