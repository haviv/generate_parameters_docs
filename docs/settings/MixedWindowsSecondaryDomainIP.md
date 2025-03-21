# Mixed Windows Secondary Domain IP

**Technical Name:** MixedWindowsSecondaryDomainIP

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Mixed Windows Secondary Domain IP parameter is used to specify the IP address of a secondary domain controller in environments where users might belong to a mixed or secondary domain beyond the primary domain configured in the Pathlock Cloud GRC platform. This setting allows for more nuanced control and handling of authentication and domain-related operations, particularly in complex network environments where multiple Windows domains exist.

**Business Impact:**

Configuring the Mixed Windows Secondary Domain IP ensures that authentication processes can accurately recognize and route authentication requests to the appropriate domain controller. This prevents login failures and access issues for users operating across multiple domains, thereby enhancing operational efficiency and user satisfaction.

**Technical Impact when configured:**

When configured, the Mixed Windows Secondary Domain IP enables the Pathlock Cloud GRC platform to effectively communicate with secondary domain controllers. This ensures that user authentications are properly processed using the secondary domain's infrastructure when the primary domain's controllers are not applicable or reachable, thereby supporting continuous access and minimizing disruptions in multi-domain environments.

**Examples Scenario:**

A company has recently acquired another company and is in the process of integrating its IT systems. The acquired company has its own Windows domain separate from the main company. By configuring the Mixed Windows Secondary Domain IP parameter, the Pathlock Cloud GRC platform can authenticate users from both companies regardless of which domain their credentials are associated with.

**Related Settings:**

- RequireDomainNameInMixedLogin

**Best Practices:** configure when operating in environments with multiple Windows domains to ensure seamless authentication. Avoid when all users are within a single domain as it may be unnecessary.