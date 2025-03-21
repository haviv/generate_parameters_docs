**Http Web Proxy Port**

**Technical Name:** HttpWebProxyPort

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The Http Web Proxy Port parameter is used for specifying the port number of the HTTP proxy that the Pathlock Cloud GRC platform should use when making outbound network calls. This setting is especially relevant in environments where direct internet access is restricted, and all outbound HTTP traffic needs to be routed through a proxy server.

**Business Impact:**

Configuring the Http Web Proxy Port correctly ensures that the Pathlock Cloud GRC platform can securely and successfully communicate with external services, such as Azure AD, through the organization's proxy server. It plays a pivotal role in maintaining the platform's functionality in restricted network environments and adheres to organizational network policies, thus preventing issues related to network communication failures.

**Technical Impact when configured:**

When set, this parameter directs the Pathlock Cloud GRC platform to route all its outgoing HTTP requests through the specified proxy server on the given port. This ensures that the platform is compatible with network infrastructure that requires the use of a proxy for internet access. Not configuring this setting correctly might lead to the inability of the platform to communicate with external services, affecting its operation and the execution of specific functionalities that depend on such communications.

**Examples Scenario:**

- **Environment Restriction:** In a corporate environment where outbound internet access is restricted through a firewall, and access is only allowed via a corporate proxy server, setting the Http Web Proxy Port ensures that Pathlock Cloud GRC can communicate with Azure AD for important functions such as user synchronization.

**Related Settings:** HttpWebProxyUrl

**Best Practices:** 

- **Configure when:** Your network environment restricts direct internet access and requires all outbound traffic to flow through an HTTP proxy.
  
- **Avoid when:** Your network infrastructure does not restrict internet access or does not utilize a proxy server for HTTP communications. In such scenarios, leaving this parameter unset can simplify the network configuration.