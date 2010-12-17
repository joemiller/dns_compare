dns_compare.py - Compare data from a BIND zone file to data returned by an authoritative DNS server.
=====================================================================================================

Purpose
-------
Use this tool to verify the data being returned by an authoritative DNS server matches
the data in a zone file.

Motivation
----------
It is very helpful when migrating from one DNS server to another to be able to
verify that all records imported correctly.

In my case, I used this tool to help me migrate multiple domains from
Windows 2000 DNS and GoDaddy DNS (which both export BIND zone files) into Amazon's
Route53 DNS service.  With this tool, I could confidently prove that all records
properly imported into Route53 before changing the whois records for each domain.

Example Usage:
--------------
Basic operation:
	``
    $ dns_compare.py -z example.com --file example.com.zone --server 10.1.1.1
    ....X...X..done
    Results:
    Matches:      9
    Mis-matches:  2
	``

Verbose:
	``
    $ dns_compare.py -z example.com --file example.com.zone --server 10.1.1.1 --verbose
	----
	[Match] querying 10.1.1.1: name='www.example.com.' type='5' class='1' ...
	Expected:  www.example.com.
	Got     :  example.com.
	----
	[Match] querying 10.1.1.1: name='mail.example.com.' type='5' class='1' ...
	Expected:  mail.example.com.
	Got     :  vlessonsatt.example.com.
	----
	[MIS-MATCH] querying 10.1.1.1: name='example.com.' type='2' class='1' ...
	Expected:  ns3.example.com.
	Got     :  ns-1633.awsdns-12.co.uk.
	``

You can also check the SOA and NS records by specifying the --soa and --ns options,
respectively.  However, if you're migrating to a different DNS server or service,
these will typically change which is why checking these record types is
disabled by default.

TODO:
-----
- In verbose output, resolve 'type' to name (eg: A, NS, MX)
- Print separate count of NXDOMAIN in results?

Author
------
Joe Miller, 
- http://github.com/joemiller
- http://www.joeym.net