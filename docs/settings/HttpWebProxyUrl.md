# Http Web Proxy Url

**Technical Name:** HttpWebProxyUrl

**Category:** Configuration

**Default Value:** None

**Impact Level:** Medium

**Description:**

The `HttpWebProxyUrl` parameter is used to specify the URL of a web proxy server that Pathlock Cloud GRC platform should use when making HTTP requests to external services. This is particularly relevant for organizations that operate within a corporate network that restricts direct internet access and requires outgoing traffic to pass through a web proxy.

**Business Impact:**

Configuring the `HttpWebProxyUrl` correctly ensures that Pathlock Cloud GRC can securely access external resources like Azure AD or other cloud services without bypassing the organizational policies on internet access. It enables seamless integration with external applications and services, ensuring that security, compliance, and risk management processes run efficiently.

**Technical Impact when configured:**

- **Security:** Utilizing a web proxy can add a layer of security by concealing the internal network's IP addresses and screening outbound and inbound traffic.
- **Compliance:** Ensures that all external communications meet the organization's compliance standards by going through controlled and monitored access points.
- **Connectivity:** Ensures that Pathlock Cloud GRC can connect to external services even from within restricted network environments.

**Examples Scenario:**

- An organization requires all outbound internet traffic to go through a central web proxy to comply with internal security policies and audit requirements. The `HttpWebProxyUrl` needs to be configured to route Pathlock Cloud GRC's requests to Azure AD through this proxy, ensuring adherence to the organizational policies.

**Related Settings:**

- `SapClientNumber`
- `SapUserName`
- `SapPassword`

**Best Practices:** 

- **Configure when:** You are operating within a restricted network environment that requires all outbound traffic to pass through a web proxy. Ensure that the proxy server is properly configured and that its URL is correctly specified in the `HttpWebProxyUrl`.
  
- **Avoid when:** Your network environment allows direct outbound internet access without the need for a proxy server, or if the use of a proxy could unintentionally block the GRC platform from accessing needed resources.