import base64, codecs
magic = 'aW1wb3J0IG9zLHN5cwpvcy5zeXN0ZW0oImNsZWFyIikKaW1wb3J0IHNtdHBsaWIKaW1wb3J0IHRpbWUKCgojQ1ZBTFVFCmJsdWU9ICdcMzNbOTRtJwpsaWdodGJsdWUgPSAnXDAzM1s5NG0nCnJlZCA9ICdcMDMzWzkxbScKd2hpdGUgPSAnXDMzWzk3bScKeWVsbG93ID0gJ1wzM1s5M20nCmdyZWVuID0gJ1wwMzNbMTszMm0nCmN5YW4gID0gIlwwMzNbOTZtIgplbmQgPSAnXDAzM1swbScKbGluZT15ZWxsb3crIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0iCnNwYWNlPSIgIgpsb2dvPXJlZCtzdHIoIiIiCiAgICAgODg4ODg4OGIuICAgLmQ4ODg4OGIuICAgLmQ4ODg4Yi4gICAgICAgWTg4YiAgIGQ4OFAgCiAgICAgODg4ICAgWTg4YiBkODhQIiAiWTg4YiBkODhQICBZODhiICAgICAgIFk4OGIgZDg4UCAgCiAgICAgODg4ICAgIDg4OCA4ODggICAgIDg4OCA4ODggICAgODg4ICAgICAgICBZODhvODhQICAgCiAgICAgODg4ICAgZDg4UCA4ODggICAgIDg4OCA4ODggICAgICAgIDg4ODg4OCAgWTg4OFAgICAgCiAgICAgODg4ODg4OFAiICA4ODggICAgIDg4OCA4ODggICAgICAgIDg4ODg4OCAgZDg4OGIgICAgCiAgICAgODg4IFQ4OGIgICA4ODggICAgIDg4OCA4ODggICAgODg4ICAgICAgICBkODg4ODhiICAgCiAgICAgODg4ICBUODhiICBZODhiLiAuZDg4UCBZODhiICBkODhQICAgICAgIGQ4OFAgWTg4YiAgCiAgICAgODg4ICAgVDg4YiAgIlk4ODg4OFAiICAgIlk4ODg4UCIgICAgICAgZDg4UCAgIFk4OGIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKIiIiKQoKICAgICAgCiAjSEVBREVSICAgICAgICAgICAgICAgIAp0ZXh0PWN5YW4rIlx0XHREZXZlbG9wZWQgQnkgOiBTYW5hdXIgQXNpZiIrZ3JlZW4rIlxuXG5cdFx04piF4piFIFJPQy1YIEthbGkgTmV0SHVudGVy4piF4piFICAgXG4iIApub3RpY2U9IiIgICAgIApkZWYgaGVhZGVyKCk6CglwcmludChsb2dvKQoJcHJpbnQodGV4dCkKCXByaW50KGxpbmUpCglwcmludChub3RpY2UpCiNTRUxFQ1RfTUFJTgpkZWYgb3B0KCk6CglwcmludChjeWFuKyJcbj09PiBTZWxlY3QgWW91ciBPcHRpb24gRnJvbSBCZWxvdyIpCglwcmludCh5ZWxsb3crIlxuXG4gWzFdIERvd25sb2FkIFJlcXVpcmVkIFNvZnR3YXJlXG5cbiBbMl0gSW5zdGFsbCBLYWxpIE5ldEh1bnRlclxuXG4gWzNdIFNldFVwIEthbGkgTmV0SHVudGVyIEtlWFxuXG4gWzRdIFN0YXJ0IE5ldEh1bnRlciBLZVggR1VJXG5cbiBbNV0gQmFjayBUbyBST0MtWCIpCmhlYWRlcigpCnByaW50KGN5YW4rIlxuXHRcdFvigKJdIENoZWNraW5nIFRoZSBSZXF1aXJlbWVudHMiKQp0aW1lLnNsZWVwKDAuNykKdHJ5OgoJZnJvbSBnb29nbGVfZHJpdmVfZG93bmxvYWRlciBpbXBvcnQgR29vZ2xlRHJpdmVEb3dubG9hZGVyIGFzIGdkZAoJaW1wb3J0IHJlcXVlc3RzCmV4Y2VwdDoKCW9zLnN5c3RlbSgiY2xlYXIiKQoJaGVhZGVyKCkKCXByaW50KGN5YW4rIlxuICBbwrBdIEluc3RhbGxpbmcgVGhlIFJlcXVpcmVtZW50cy4gQWxsb3cgVXAgdG8gMTAgbWludXRlcyAiKQoJdGltZ'
love = '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'
god = 'Npb24gNS4wK1xuXG4gIFsyXSBBdCBMZWFzdCAzIEdCIEludGVybmFsIFN0b3JhZ2VcblxuICBbM10gQXQgTGVhc3QgMiBHQiBEYXRhXG5cbiAgWzRdIEF0IExlYXN0IDMwLTYwIE1pbnV0ZXNcblxuIityZWQrIiBbIV0gWW91IHdpbGwgYmUgbm90IGFibGUgdG8gUXVpdCBvciBNaW5pbWl6ZSBUZXJtdXggZHVyaW5nIHRoZSBJbnN0YWxsYXRpb24uIFNvLCBJbnN0YWxsIGl0IGF0IHlvdXIgZnJlZSB0aW1lLiIpCgkJbmhvcHQ9c3RyKGlucHV0KGJsdWUrIlxuIFs+XSBEbyBZb3UgV2FudCB0byBDb250aW51ZSA/IFt5L25dIDogIit5ZWxsb3cpKQoJCWlmIG5ob3B0PT0ieSIgb3IgbmhvcHQ9PSJZIiBvciBuaG9wdD09InllcyIgb3IgbmhvcHQ9PSJZRVMiOgoJCQlvcy5zeXN0ZW0oImNsZWFyIikKCQkJaGVhZGVyKCkKCQkJcHJpbnQoY3lhbisiXG4gWz5dIEl0IENhbiBUYWtlIFVwIHRvIDMwLTEyMCBNaW51dGVzICEgU28sIEJlIFBhdGllbnQuXG5cbiBbPl0gRG9uJ3QgQ2xvc2Ugb3IgTWluaW1pemUgVGVybXV4IGR1cmluZyBJbnN0YWxsYXRpb25cblxuIFs+XSBBbHdheXMgRW50ZXIgXCJZXCIgSWYgQW55IFF1ZXN0aW9uIFJhaXNlLlxuXG4iKQoJCQluaG9wPXN0cihpbnB1dChibHVlKyJcbiBbPl0gRG8gWW91IFdhbnQgdG8gQ29udGludWUgPyBbeS9uXSA6ICIreWVsbG93KSkKCQkJaWYgbmhvcD09InkiIG9yIG5ob3B0PT0iWSIgb3IgbmhvcHQ9PSJ5ZXMiIG9yIG5ob3B0PT0iWUVTIjoKCQkJCW9zLnN5c3RlbSgiY2xlYXIiKQoJCQkJaGVhZGVyKCkKCQkJCXByaW50KGN5YW4rIlx0XHRbPl0gSW5zdGFsbGluZyBLYWxpIE5ldEh1bnRlciBcblxuIitlbmQpCgkJCQl0cnk6CgkJCQkJcHJpbnQoZ3JlZW4pCgkJCQkJb3Muc3lzdGVtKCJjZCAkSE9NRSAmJiBwa2cgaW5zdGFsbCB3Z2V0IC15IikKCQkJCQlvcy5zeXN0ZW0oImNkICRIT01FICYmIHdnZXQgLU8gaW5zdGFsbC1uZXRodW50ZXItdGVybXV4IGh0dHBzOi8vb2Zmcy5lYy8yTWNlWldyIikKCQkJCQlwcmludChncmVlbikKCQkJCQlvcy5zeXN0ZW0oImNkICRIT01FICYmIGNobW9kICt4IGluc3RhbGwtbmV0aHVudGVyLXRlcm11eCIpCgkJCQkJcHJpbnQoZ3JlZW4pCgkJCQkJb3Muc3lzdGVtKCJjZCAkSE9NRSAmJiAuL2luc3RhbGwtbmV0aHVudGVyLXRlcm11eCIpCgkJCQkJbGFzdHQ9c3RyKGlucHV0KGN5YW4rIlxuXG5cdFx0IitncmVlbisiW+Kck10gSW5zdGFsbGVkIFN1Y2Nlc3NmdWxseSEiK2N5YW4rIlxuXG5cdCAgICBb4oCiXSBOb3cgUHJlc3MgRW50ZXIgS2V5IFRvIENvbnRpbnVlXG4iKSkKCQkJCQlvcy5zeXN0ZW0oImNsZWFyIikKCQkJCQlvcy5zeXN0ZW0oInB5dGhvbiBrYWxpLnB5IikKCQkJCWV4Y2VwdDoKCQkJCQlsYXN0dD1zdHIoaW5wdXQoY3lhbisiXG5cblx0XHQiK3JlZCsiW8OXXSBBbiBVbmtub3duIEVycm9yIE9jY3VycmVkICEiK2N5YW4rIlxuXG5cdCAgICBb4oCiXSBOb3cgUHJlc3MgRW50ZXIgS2V5IFRvIENvbnRpbnVlXG4iKSkKCQkJCQlvcy5zeXN0ZW0oImNsZWFyIikKCQkJCQlvcy5zeXN0ZW0oInB5dGhvbiBrYWxpLnB5IikKCQkJZWxzZToKCQkJCW9zLnN5c3RlbSgiY2xlYXIiKQoJCQkJb3Muc3lzdGVtKCJweXRob24ga2FsaS5weSIpCgkJZWxzZToKCQkJb3Muc3lzdGVtKCJjbGVhciI'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
