import json

data = """
{
    "results": [
        {
            "id": "1364722844",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "712020:18682b8d-c1c4-432b-8a74-b72ad9e829d9",
                "createdAt": "2025-05-06T14:09:29.345Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>using AWS <strong><u>service managed</u></strong> admin role</p>"
                }
            },
            "resolutionStatus": "resolved",
            "resolutionLastModifierId": "70121:beb06c0a-3e04-4284-8d93-296e45ec14b8",
            "resolutionLastModifiedAt": "2025-05-08T11:11:51.457Z",
            "properties": {
                "inlineMarkerRef": "7865e09b-1486-4671-8e68-5fd79fe94640",
                "inlineOriginalSelection": "deploying stacks of default resources",
                "inline-marker-ref": "7865e09b-1486-4671-8e68-5fd79fe94640",
                "inline-original-selection": "deploying stacks of default resources"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1364722844"
            }
        },
        {
            "id": "1365253709",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:045cf23e-02d1-4092-8e52-ec7107f31052",
                "createdAt": "2025-05-07T09:14:39.291Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Is the intent behind including Slingshot so that these accounts can then be used for deploying Slingshotted IaC/CloudFormation? </p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "91c304dc-013b-4317-a6d5-50784dae29eb",
                "inlineOriginalSelection": "Slingshot",
                "inline-marker-ref": "91c304dc-013b-4317-a6d5-50784dae29eb",
                "inline-original-selection": "Slingshot"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365253709"
            }
        },
        {
            "id": "1365253772",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "6408e0e34d5e4b44e234cdcc",
                "createdAt": "2025-05-07T09:16:22.505Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Not security specific, but I don't see any mentions to cost governance. Are there going to be any controls to prevent overspending?</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "095257cc-112e-4f85-aa0e-2590b81f969c",
                "inlineOriginalSelection": "Governance of newly provisioned accounts",
                "inline-marker-ref": "095257cc-112e-4f85-aa0e-2590b81f969c",
                "inline-original-selection": "Governance of newly provisioned accounts"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365253772"
            }
        },
        {
            "id": "1365319590",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:18:19.714Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Wouldn&rsquo;t a gitops solution be more reasonable given that this accounts will have a squad as owner and would benefit from having catalogs?</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "b42a6b85-8769-499d-b009-517650979dd8",
                "inlineOriginalSelection": "use Self Service",
                "inline-marker-ref": "b42a6b85-8769-499d-b009-517650979dd8",
                "inline-original-selection": "use Self Service"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365319590"
            }
        },
        {
            "id": "1365351560",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:18:38.556Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>why?</p>"
                }
            },
            "resolutionStatus": "resolved",
            "resolutionLastModifierId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
            "resolutionLastModifiedAt": "2025-05-07T09:24:47.842Z",
            "properties": {
                "inlineMarkerRef": "3d88a88b-4e92-4324-bdd3-d9131c5ab160",
                "inlineOriginalSelection": "randomly generated name",
                "inline-marker-ref": "3d88a88b-4e92-4324-bdd3-d9131c5ab160",
                "inline-original-selection": "randomly generated name"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365351560"
            }
        },
        {
            "id": "1365319669",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:045cf23e-02d1-4092-8e52-ec7107f31052",
                "createdAt": "2025-05-07T09:19:39.006Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>I&rsquo;m slightly confused, or missing something in this DR, but with the StackSets would all of the bellow resources need to be defined in a new PoC-specific CloudFormation template? Does that piece of work itself need some design as well?</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "4aa3c420-cc87-4ffd-87a1-6fe75b94989d",
                "inlineOriginalSelection": "default resources",
                "inline-marker-ref": "4aa3c420-cc87-4ffd-87a1-6fe75b94989d",
                "inline-original-selection": "default resources"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365319669"
            }
        },
        {
            "id": "1365351617",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 2,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:20:35.952Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>This looks like a design flaw. Given how uncommon this are, if we fail to process this events correctly we could fail to clean up. A scheduled batch/lambda running daily (with proper alerting and metrics) would likely be a safer choice.</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "2b6678c7-3fb7-4c8a-92a8-16a64823d150",
                "inlineOriginalSelection": "two EventBridge events",
                "inline-marker-ref": "2b6678c7-3fb7-4c8a-92a8-16a64823d150",
                "inline-original-selection": "two EventBridge events"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365351617"
            }
        },
        {
            "id": "1365254123",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:21:33.978Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>What&rsquo;s the IAM scaffolding we&rsquo;re gonna use to make this possible?</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "3f7bd752-9b01-4ffc-8b99-75e186cb4981",
                "inlineOriginalSelection": "User is now able to log in using the near-admin role and use the account.",
                "inline-marker-ref": "3f7bd752-9b01-4ffc-8b99-75e186cb4981",
                "inline-original-selection": "User is now able to log in using the near-admin role and use the account."
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365254123"
            }
        },
        {
            "id": "1365286747",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:23:35.242Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Could we explicitly explain what OU structure we&rsquo;ll create to host this accounts and what SCPs will there be by default?</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "c4d9670b-d1cc-41d0-84c8-a1ffad1816ae",
                "inlineOriginalSelection": "new account",
                "inline-marker-ref": "c4d9670b-d1cc-41d0-84c8-a1ffad1816ae",
                "inline-original-selection": "new account"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365286747"
            }
        },
        {
            "id": "1365286779",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:24:24.108Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>It might be useful to include a few actual use cases where this would be useful.</p>"
                }
            },
            "resolutionStatus": "resolved",
            "resolutionLastModifierId": "70121:beb06c0a-3e04-4284-8d93-296e45ec14b8",
            "resolutionLastModifiedAt": "2025-05-08T10:49:41.411Z",
            "properties": {
                "inlineMarkerRef": "a9c29376-bb80-47d0-9a24-79fc55e17d64",
                "inlineOriginalSelection": "PoC accounts",
                "inline-marker-ref": "a9c29376-bb80-47d0-9a24-79fc55e17d64",
                "inline-original-selection": "PoC accounts"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365286779"
            }
        },
        {
            "id": "1365319938",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:26:53.259Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>All of this are quite simple to check before creating the account.</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "f258e2d6-7ceb-424f-8685-62f576acb2fd",
                "inlineOriginalSelection": "Selected name may not be uniqueName selected may be in use by a previous account which is still in the process of deletion, even if it appears availableRisk of chosen name + general prefix exceeding AD character limit",
                "inline-marker-ref": "f258e2d6-7ceb-424f-8685-62f576acb2fd",
                "inline-original-selection": "Selected name may not be uniqueName selected may be in use by a previous account which is still in the process of deletion, even if it appears availableRisk of chosen name + general prefix exceeding AD character limit"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365319938"
            }
        },
        {
            "id": "1365286872",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 2,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T12:59:11.881Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Simplifying creation to make it a 1-click solution makes every single action in the next 90 days harder as finding the right account won&rsquo;t be trivial being identified only by a random number and random name.</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "1fb026a7-6486-41fd-967d-0e80682dbdbf",
                "inlineOriginalSelection": "Tracking more difficult",
                "inline-marker-ref": "1fb026a7-6486-41fd-967d-0e80682dbdbf",
                "inline-original-selection": "Tracking more difficult"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365286872"
            }
        },
        {
            "id": "1365286898",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:28:29.641Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Missing con: You can&rsquo;t have 2 PoCs for a single project at the same time.</p>"
                }
            },
            "resolutionStatus": "resolved",
            "resolutionLastModifierId": "70121:beb06c0a-3e04-4284-8d93-296e45ec14b8",
            "resolutionLastModifiedAt": "2025-05-08T13:45:55.091Z",
            "properties": {
                "inlineMarkerRef": "3d3b0b8c-a756-449b-aa24-9dd22e701db5",
                "inlineOriginalSelection": "project name",
                "inline-marker-ref": "3d3b0b8c-a756-449b-aa24-9dd22e701db5",
                "inline-original-selection": "project name"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365286898"
            }
        },
        {
            "id": "1365286935",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "557058:ae23886d-640f-4eca-bc0e-c1768b18c19b",
                "createdAt": "2025-05-07T09:29:33.872Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Do we have a reason for going for account deletion over (for instance), wiping an account back to a base zero cost level and keeping it in a warm pool?</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "6b56bb5f-2546-43f2-a0d9-0f9790c918b5",
                "inlineOriginalSelection": "deletion",
                "inline-marker-ref": "6b56bb5f-2546-43f2-a0d9-0f9790c918b5",
                "inline-original-selection": "deletion"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365286935"
            }
        },
        {
            "id": "1365320122",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:31:07.016Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Organisations API + Stack Sets are also new technologies. Terraform on the other hand is widely used across the business.</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "8732c9f1-6fda-43f7-ad0e-0bbc7133f130",
                "inlineOriginalSelection": "new technology",
                "inline-marker-ref": "8732c9f1-6fda-43f7-ad0e-0bbc7133f130",
                "inline-original-selection": "new technology"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365320122"
            }
        },
        {
            "id": "1365254921",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:31:23.824Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Why is this bad?</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "4bc29ca8-9f16-4ef9-af68-f668567c7b28",
                "inlineOriginalSelection": "Requires PR workflows",
                "inline-marker-ref": "4bc29ca8-9f16-4ef9-af68-f668567c7b28",
                "inline-original-selection": "Requires PR workflows"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365254921"
            }
        },
        {
            "id": "1365254978",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:32:02.317Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Can&rsquo;t we create a PR automatically at the right time?</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "e683b1bd-599f-465e-9b78-8e51793f761a",
                "inlineOriginalSelection": "Cleanup of account definition after automated deletion",
                "inline-marker-ref": "e683b1bd-599f-465e-9b78-8e51793f761a",
                "inline-original-selection": "Cleanup of account definition after automated deletion"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365254978"
            }
        },
        {
            "id": "1365352467",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:32:58.869Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>This is a con, it means you&rsquo;ll be creating infrastructure without the possibility of peer review.</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "2a192518-89d0-4814-b211-42694b05de3c",
                "inlineOriginalSelection": "Doesn't require PR workflows",
                "inline-marker-ref": "2a192518-89d0-4814-b211-42694b05de3c",
                "inline-original-selection": "Doesn't require PR workflows"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365352467"
            }
        },
        {
            "id": "1365320218",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T09:33:43.919Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>How are we going to deploy the slingshot/cfripper/&hellip; primitives that are currently strata based?</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "a9811777-a26c-4b65-9cb8-19a54dbe9fed",
                "inlineOriginalSelection": "Custom solution",
                "inline-marker-ref": "a9811777-a26c-4b65-9cb8-19a54dbe9fed",
                "inline-original-selection": "Custom solution"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365320218"
            }
        },
        {
            "id": "1365361972",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "70121:63605fc5-aafb-402c-87ba-466682824f5f",
                "createdAt": "2025-05-07T13:24:30.254Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>This would be interesting to fill</p>"
                }
            },
            "resolutionStatus": "resolved",
            "resolutionLastModifierId": "70121:beb06c0a-3e04-4284-8d93-296e45ec14b8",
            "resolutionLastModifiedAt": "2025-05-13T13:07:23.950Z",
            "properties": {
                "inlineMarkerRef": "ccae483d-9558-4e53-8845-bc0c9f702e28",
                "inlineOriginalSelection": "Operational Metrics",
                "inline-marker-ref": "ccae483d-9558-4e53-8845-bc0c9f702e28",
                "inline-original-selection": "Operational Metrics"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1365361972"
            }
        },
        {
            "id": "1368670362",
            "status": "current",
            "title": "Re: PoC Account Vending - Design Review",
            "pageId": "1362950472",
            "version": {
                "number": 1,
                "message": "",
                "minorEdit": false,
                "authorId": "6061e38d610003006804744c",
                "createdAt": "2025-05-13T12:37:09.915Z"
            },
            "body": {
                "storage": {
                    "representation": "storage",
                    "value": "<p>Anything else needing thought of in here to &ldquo;keep our house in order&rdquo;? Just thinking about stuff that falls down the back of the sofa e.g. AD groups, projects, self service config, other repo config etc.</p>"
                }
            },
            "resolutionStatus": "open",
            "properties": {
                "inlineMarkerRef": "d083d3e5-0b56-4616-8d4c-ce62f8ca56ff",
                "inlineOriginalSelection": "deprovision the account",
                "inline-marker-ref": "d083d3e5-0b56-4616-8d4c-ce62f8ca56ff",
                "inline-original-selection": "deprovision the account"
            },
            "_links": {
                "webui": "/spaces/CAS/pages/1362950472/PoC+Account+Vending+-+Design+Review?focusedCommentId=1368670362"
            }
        }
    ],
    "_links": {
        "base": "https://skyscanner.atlassian.net/wiki"
    }
}
"""

data = json.loads(data)
print(data)
comments = []
for c in data['results']:
    excerpt = c.get('properties', {}).get('inlineOriginalSelection')
    comment = c.get('body', {}).get('storage', {}).get('value')
    if excerpt and comment:
        comments.append({
            "Excerpt": excerpt,
            "Comment": comment
        })
print(comments)