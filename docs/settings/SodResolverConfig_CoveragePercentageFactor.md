# Coverage percentage factor

**Technical Name:** SodResolverConfig_CoveragePercentageFactor

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

The Coverage Percentage Factor parameter specifies the threshold for accepting SoD (Segregation of Duties) resolution solutions based on a percentage rating. It determines the minimal acceptance level of solution coverage, influencing the narrow down of potential solutions during the SoD conflict resolution process.

**Business Impact:**

This setting directly impacts the rigidity or flexibility of the SoD conflict resolution process. Adjusting the Coverage Percentage Factor can result in either a stringent approach that minimizes risk but may restrict business operations, or a more lenient approach that maintains operational efficiency but could potentially allow for greater risk exposure.

**Technical Impact when configured:**

When configured, the parameter adjusts the SoD Resolver's solution filtering process, impacting how transactions are considered for exclusion or retention in resolving SoD conflicts. A higher percentage signifies a preference for solutions that address a larger portion of the conflict, while a lower percentage may result in solutions that cover less but potentially maintain more business functionality.

**Examples Scenario:**

An organization sets the Coverage Percentage Factor to a high value, indicating that only solutions covering a high percentage of the SoD conflict are acceptable. This may result in more transactions being suggested for removal, potentially impacting operational efficiency but ensuring a high level of compliance and risk mitigation.

**Related Settings:**

- SodMitigatedUsersGroupId
- SodResolver_MaxNoOfActivitiesToKeep

**Best Practices:** Configure the Coverage Percentage Factor to balance between operational efficiency and risk mitigation based on the organization's risk tolerance. Avoid setting the factor too low in environments where compliance is critical, and conversely, avoid setting it too high in dynamic business environments where flexibility is key.