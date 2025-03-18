# Activity To User Matrix Static And Real User Use Static As Base For The Report

**Technical Name:** ActivityToUserMatrixStaticAndRealUserUseStaticAsBaseForTheReport

**Category:** Reporting

**Default Value:** False

**Impact Level:** High

**Description:**

This setting controls how the comparison between a static user activity matrix and real-time user data is handled in the reporting feature. When enabled, the static matrix serves as the base reference, and overlaps with real user activities are marked distinctly.

**Business Impact:**

Allows organizations to effectively track and analyze deviations in user activities from established baselines, highlighting potential security or compliance risks. This insight is crucial for maintaining stringent GRC (Governance, Risk Management, and Compliance) standards within an organization's IT ecosystem.

**Technical Impact when configured:**

When this setting is enabled, any activity recorded for users that matches the static matrix's activities will be marked, facilitating straightforward identification of conformity and deviations. This helps in pinpointing unauthorized or unexpected actions within the system, thereby enhancing oversight.

**Examples Scenario:**

An organization wants to ensure that users are only performing actions within their purview, as delineated by predefined roles and permissions. By enabling this setting, they can easily compare actual user activities against the statically defined matrix of activities meant for those roles, identifying any discrepancies or unauthorized actions.

**Related Settings:** N/A

**Best Practices:** configure when you need rigorous oversight on user activities vis-a-vis their defined roles and permissions to ensure security and compliance. Avoid when such detailed tracking is not essential, as it may lead to unnecessary data processing and interpretation efforts.