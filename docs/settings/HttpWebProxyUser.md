# Http Web Proxy User

**Technical Name:** HttpWebProxyUser

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Http Web Proxy User parameter is used for configuring the credentials of a user account that has the necessary permissions to access web services through a proxy. This setting is crucial for environments where direct internet access is restricted and a web proxy is used to control and monitor web traffic.

**Business Impact:**

Configuring the Http Web Proxy User parameter correctly is essential for ensuring uninterrupted access to external web services that are critical for the Pathlock Cloud GRC platform's operations. It impacts the platform's ability to retrieve necessary data, perform updates, and communicate with external services securely.

**Technical Impact when configured:**

When configured, this parameter enables the Pathlock Cloud GRC platform to authenticate and route its web service requests through the specified proxy server using the provided user credentials. This supports adherence to organizational security policies and allows for the monitoring and control of web traffic.

**Examples Scenario:**

- **Compliance Monitoring:** To ensure compliance with security policies, an organization restricts all external internet access through a web proxy. The Http Web Proxy User parameter must be configured with proxy user credentials to allow the Pathlock Cloud GRC platform to access necessary web services for compliance data updates.
  
- **Secure Data Access:** An organization uses a web proxy to monitor and secure web traffic. To securely access cloud-based GRC data sources, the Http Web Proxy User is configured, ensuring data is accessed safely without bypassing security protocols.

**Related Settings:**

**Applicable Workflows Actions:** 

**Best Practices:** 

- **Configure when:** You are operating in a controlled environment where web access is restricted through a proxy server. It ensures that the platform can securely access external web services without violating security policies.
  
- **Avoid when:** If your network environment does not use a web proxy for internet access, configuring this parameter is not necessary.