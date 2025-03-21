**Organization Structure Secondary Provider Include Empty Values**

**Technical Name:** OrganizationStructureSecondaryProvider_IncludeEmptyValues

**Category:** Configuration

**Default Value:** "-"

**Impact Level:** Medium

**Description:**

This parameter controls the inclusion of empty values when syncing data from a secondary provider into the organization's structure within the Pathlock Cloud GRC platform. It determines how empty or null values from secondary data sources are treated, ensuring that organizational data integrity and completeness are maintained.

**Business Impact:**

Having the correct configuration for this parameter is crucial for maintaining the accuracy and reliability of an organization's structure data within the Pathlock GRC system. It impacts how comprehensive and clean the synchronized data is, affecting reporting, compliance, and risk management processes.

**Technical Impact when configured:**

When this parameter is configured to include empty values, all records, including those with null or empty fields from the secondary data provider, are synchronized. This might lead to the presence of incomplete data in the system but ensures no data is accidentally excluded due to being incomplete.

**Example Scenario:**

Consider an organization that utilizes multiple systems for user management and wishes to synchronize user roles from a secondary system into Pathlock GRC. If certain user roles in the secondary system are not assigned (null or empty), configuring this parameter to include empty values ensures these user records are still imported into Pathlock GRC, potentially highlighting where roles need to be reviewed or assigned.

**Related Settings:** OrganizationStructureSecondaryProvider_CharsToRemove

**Best Practices:** 
- Configure to include empty values when comprehensive data synchronization is critical, even at the expense of importing incomplete records.
- Avoid including empty values when data purity and completeness are more crucial than ensuring every record is imported.