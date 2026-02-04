# MCP (Model Context Protocol) Support

Connect to remote tools and services via the Model Context Protocol.

## 🔌 Overview

MCP (Model Context Protocol) enables PyGPT to connect to remote tools and services, extending AI capabilities beyond built-in features. Access external APIs, databases, and services through a standardized protocol.

**Key Features:**
- Remote tool access
- Multiple transport types
- Per-server filtering
- Authorization support
- Tools caching
- Secure connections

**Status:** Production-ready  
**Plugin:** MCP (built-in)

## 🆚 vs Built-in Plugins

### MCP Tools (Remote)
- ✅ External services
- ✅ Remote APIs
- ✅ Third-party tools
- ✅ Standardized protocol
- ✅ Easy integration
- ✅ Community tools

### Built-in Plugins (Local)
- Local execution
- Direct access
- No network needed
- Faster execution
- More control

## 🚀 Getting Started

### Prerequisites

1. **MCP Server**
   - Running MCP server
   - Or use public MCP services
   - Server URL/endpoint

2. **Configuration**
   - Server details
   - Authentication (if required)
   - Transport type

### Enable MCP Plugin

1. Launch PyGPT
2. Menu: `Plugins → MCP`
3. Enable plugin
4. Configure servers

## 🎯 Use Cases

### External APIs
```
Connect to:
- Weather services
- Stock market data
- News APIs
- Translation services
```

### Databases
```
Query databases:
- SQL databases
- NoSQL databases
- Vector databases
- Time-series databases
```

### Cloud Services
```
Access cloud:
- AWS services
- Google Cloud
- Azure services
- Cloud storage
```

### Custom Tools
```
Your own tools:
- Internal APIs
- Custom services
- Business logic
- Proprietary data
```

## ⚙️ Configuration

### Settings Location
`Plugins → MCP → Settings`

### Server Configuration

Each MCP server needs:
- **Name** - Server identifier
- **Transport** - Connection type
- **Endpoint** - Server URL/path
- **Auth** - Authentication details
- **Filters** - Tool allow/deny lists

### Adding a Server

1. **Open MCP Settings**
   ```
   Plugins → MCP → Settings → Add Server
   ```

2. **Configure Server**
   ```
   Name: weather-api
   Transport: HTTP
   Endpoint: https://api.weather.com/mcp
   Auth: Bearer token
   ```

3. **Set Filters (Optional)**
   ```
   Allow: get_weather, get_forecast
   Deny: admin_*
   ```

4. **Save Configuration**

## 🔧 Transport Types

### stdio (Standard I/O)

Local process communication.

**Use for:**
- Local MCP servers
- Command-line tools
- Local scripts

**Configuration:**
```
Transport: stdio
Command: python mcp_server.py
Args: --port 8080
```

**Example:**
```
Name: local-tools
Transport: stdio
Command: /usr/bin/mcp-server
Working Dir: /opt/mcp
```

### SSE (Server-Sent Events)

One-way server push.

**Use for:**
- Real-time updates
- Streaming data
- Event notifications

**Configuration:**
```
Transport: SSE
Endpoint: https://api.example.com/mcp/events
```

**Example:**
```
Name: live-data
Transport: SSE
Endpoint: https://data.example.com/stream
Auth: Bearer abc123
```

### HTTP (Streamable HTTP)

Standard HTTP requests.

**Use for:**
- REST APIs
- Web services
- Most remote tools

**Configuration:**
```
Transport: HTTP
Endpoint: https://api.example.com/mcp
Method: POST
Headers: Authorization: Bearer token
```

**Example:**
```
Name: api-tools
Transport: HTTP
Endpoint: https://tools.example.com/mcp
Auth: Bearer xyz789
```

## 📋 Tool Filtering

### Allow List

Only specified tools are available.

**Configuration:**
```
Allow:
- get_weather
- get_forecast
- search_location
```

**Use when:**
- Security is critical
- Limited tool set needed
- Explicit control required

### Deny List

All tools except specified are available.

**Configuration:**
```
Deny:
- delete_*
- admin_*
- dangerous_operation
```

**Use when:**
- Most tools are safe
- Few tools to block
- Flexible access needed

### Wildcards

Use patterns to match multiple tools.

**Examples:**
```
Allow:
- get_*        # All getters
- search_*     # All search tools
- weather.*    # All weather tools

Deny:
- *_delete     # All delete operations
- admin.*      # All admin tools
- *.dangerous  # All dangerous tools
```

## 🔐 Authentication

### Bearer Token

Most common authentication method.

**Configuration:**
```
Auth Type: Bearer
Token: your-api-token-here
```

**Header:**
```
Authorization: Bearer your-api-token-here
```

### API Key

Simple API key authentication.

**Configuration:**
```
Auth Type: API Key
Key Name: X-API-Key
Key Value: your-api-key
```

**Header:**
```
X-API-Key: your-api-key
```

### Custom Headers

Any custom authentication headers.

**Configuration:**
```
Headers:
  Authorization: Bearer token
  X-Custom-Auth: value
  X-Request-ID: uuid
```

### No Authentication

Public or local servers.

**Configuration:**
```
Auth Type: None
```

## 🎨 Examples

### Example 1: Weather Service

**Server Configuration:**
```
Name: weather-mcp
Transport: HTTP
Endpoint: https://api.weather.com/mcp
Auth: Bearer YOUR_TOKEN

Allow:
- get_current_weather
- get_forecast
- search_location
```

**Usage:**
```
User: "What's the weather in New York?"

AI: [Calls get_current_weather via MCP]
Response: "Currently 72°F and sunny in New York..."
```

### Example 2: Database Access

**Server Configuration:**
```
Name: database-mcp
Transport: HTTP
Endpoint: https://db.example.com/mcp
Auth: Bearer DB_TOKEN

Allow:
- query_users
- query_orders
- get_statistics

Deny:
- delete_*
- drop_*
- truncate_*
```

**Usage:**
```
User: "How many orders did we have last month?"

AI: [Calls query_orders via MCP]
Response: "You had 1,247 orders last month..."
```

### Example 3: Local Tools

**Server Configuration:**
```
Name: local-tools
Transport: stdio
Command: python /opt/mcp/server.py
Working Dir: /opt/mcp

Allow:
- file_operations
- system_info
- process_data
```

**Usage:**
```
User: "Process the data in data.csv"

AI: [Calls process_data via MCP]
Response: "Data processed successfully. Results saved to output.csv"
```

## 🔧 Tools Cache

### What It Does

Caches available tools from MCP servers for faster access.

**Benefits:**
- Faster tool discovery
- Reduced API calls
- Better performance
- Offline tool list

### Configuration

**Enable Cache:**
```
Plugins → MCP → Settings → Enable Tools Cache
```

**Cache Duration:**
```
Cache TTL: 3600 seconds (1 hour)
```

**Clear Cache:**
```
Plugins → MCP → Settings → Clear Cache
```

## 🐛 Troubleshooting

### Connection Failed
**Problem:** Can't connect to MCP server

**Solutions:**
- Check server is running
- Verify endpoint URL
- Check network connectivity
- Verify authentication

### Tool Not Found
**Problem:** Tool not available

**Solutions:**
- Check tool name spelling
- Verify allow/deny filters
- Clear tools cache
- Check server configuration

### Authentication Error
**Problem:** Auth failed

**Solutions:**
- Verify token/key is valid
- Check token hasn't expired
- Verify header format
- Check server logs

### Slow Performance
**Problem:** Tools are slow

**Solutions:**
- Enable tools cache
- Check network latency
- Optimize server
- Use local transport if possible

## 💡 Best Practices

### Security

```
✅ Use authentication
✅ Implement allow lists
✅ Deny dangerous operations
✅ Use HTTPS
✅ Rotate tokens regularly
❌ Expose without auth
❌ Allow all tools
```

### Performance

```
✅ Enable tools cache
✅ Use local transport when possible
✅ Limit tool set
✅ Optimize server
❌ Disable cache
❌ Use slow networks
```

### Configuration

```
✅ Descriptive server names
✅ Document tool purposes
✅ Test before production
✅ Monitor usage
❌ Generic names
❌ No documentation
```

### Error Handling

```
✅ Handle connection errors
✅ Provide fallbacks
✅ Log failures
✅ Retry on timeout
❌ Assume success
❌ Ignore errors
```

## 🔗 Related Features

- [Plugins Guide](../guides/06-plugins-extensions.md) - Plugin system
- [Custom Commands](./08-custom-commands.md) - Custom tools
- [Remote Tools](../reference/remote-tools.md) - Remote tool configuration

## 📚 Additional Resources

- [MCP Specification](https://modelcontextprotocol.io/)
- [MCP Servers List](https://github.com/modelcontextprotocol/servers)
- [Building MCP Servers](https://modelcontextprotocol.io/docs/building-servers)

## ⚠️ Limitations

- **Network required** - For remote servers
- **Latency** - Network delays
- **Availability** - Depends on server uptime
- **Security** - Trust server provider
- **Compatibility** - Server must support MCP

## 💰 Cost Considerations

MCP tool calls may incur costs:
- API usage charges
- Network bandwidth
- Server hosting
- Third-party service fees

**Cost-saving tips:**
- Cache tool definitions
- Limit tool calls
- Use local servers when possible
- Monitor usage

## 🆘 Need Help?

- Check [Plugins Guide](../guides/06-plugins-extensions.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Custom Commands](./08-custom-commands.md) →
