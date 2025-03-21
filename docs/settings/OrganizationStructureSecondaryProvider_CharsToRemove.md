# Organization Structure Secondary Provider Chars To Remove

**Technical Name:** OrganizationStructureSecondaryProvider_CharsToRemove

**Category:** Configuration

**Default Value:** 0

**Impact Level:** Medium

**Description:** This configuration parameter specifies the number of characters to be removed from the organization structure identifiers fetched from the secondary provider during the synchronization process.

**Business Impact:** Proper configuration of this parameter ensures accurate matching and mapping of organizational structure data between primary and secondary data sources. Misconfiguration can lead to mismatched or incomplete organizational hierarchy representations, impacting security, compliance, and reporting functionalities.

**Technical Impact when configured:** When set, this parameter dynamically trims the specified number of characters from the end of organization structure identifiers retrieved from the secondary provider. This adjustment is crucial when integrating data from multiple sources with varying identifier formats, facilitating seamless synchronization and consistent data representation across the Pathlock GRC platform.

**Example Scenario:** Suppose your primary data source uses 10-character organizational identifiers, while your secondary provider appends a 2-character country code at the end. Setting this parameter to "2" ensures these extraneous characters are removed, maintaining consistent identifier formats across your GRC environment.

**Related Settings:** 

- `SecondaryProviderAdditionalComparisonField` (referenced within syncing processes for data alignment enhancements).

**Best Practices:** Configure when integrating data from secondary providers with identifier formats differing from your primary source. Avoid when identifier formats are consistent across data sources, or the removal of characters may result in data integrity issues.