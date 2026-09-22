--
-- PostgreSQL database dump
--

\restrict 5ha7eQcKKEHR607cPYEEaLsw1FPqiMzxSMhgtigODqd7RVcvfdCtkAJQiaqPfGc

-- Dumped from database version 16.15 (Ubuntu 16.15-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.15 (Ubuntu 16.15-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: cita_bitacora; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cita_bitacora (id, cita_id, ts, por, canal, accion, detalle) FROM stdin;
1	imp-1	2026-05-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
2	imp-10	2026-05-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
3	imp-100	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
4	imp-1000	2026-07-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
5	imp-1001	2026-08-05 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
6	imp-1002	2026-08-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
7	imp-1003	2026-08-13 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
8	imp-1004	2026-08-12 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
9	imp-1005	2026-08-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
10	imp-1006	2026-08-12 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
11	imp-1007	2026-08-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
12	imp-1008	2026-08-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
13	imp-1009	2026-08-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
14	imp-101	2026-06-03 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
15	imp-1010	2026-07-29 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
16	imp-1011	2026-07-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
17	imp-1012	2026-07-29 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
18	imp-1013	2026-08-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
19	imp-1014	2026-08-04 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
20	imp-1015	2026-08-10 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
21	imp-1016	2026-08-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
22	imp-1017	2026-08-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
23	imp-1018	2026-08-08 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
24	imp-1019	2026-08-12 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
25	imp-102	2026-05-25 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
26	imp-1020	2026-07-29 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
27	imp-1021	2026-07-29 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
28	imp-1022	2026-07-29 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
29	imp-1023	2026-08-13 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
30	imp-1024	2026-07-30 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
31	imp-1025	2026-07-29 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
32	imp-1026	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
33	imp-1027	2026-08-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
34	imp-1028	2026-08-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
35	imp-1029	2026-07-30 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
36	imp-103	2026-06-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
37	imp-1030	2026-08-03 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
38	imp-1031	2026-07-29 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
39	imp-1032	2026-07-29 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
40	imp-1033	2026-07-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
41	imp-1034	2026-07-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
42	imp-1035	2026-08-08 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
43	imp-1036	2026-08-08 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
44	imp-1037	2026-08-18 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
45	imp-1038	2026-08-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
46	imp-1039	2026-08-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
47	imp-104	2026-06-01 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
48	imp-1040	2026-08-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
49	imp-1041	2026-08-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
50	imp-1042	2026-08-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
51	imp-1043	2026-08-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
52	imp-1044	2026-08-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
53	imp-1045	2026-08-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
54	imp-1046	2026-08-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
55	imp-1047	2026-08-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
56	imp-1048	2026-08-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
57	imp-1049	2026-08-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
58	imp-105	2026-06-04 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
59	imp-1050	2026-08-12 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
60	imp-1051	2026-08-12 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
61	imp-1052	2026-08-12 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
62	imp-1053	2026-08-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
63	imp-1054	2026-08-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
64	imp-1055	2026-08-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
65	imp-1056	2026-08-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
66	imp-1057	2026-08-20 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
67	imp-1058	2026-08-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
68	imp-1059	2026-08-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
69	imp-106	2026-06-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
70	imp-1060	2026-08-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
71	imp-1061	2026-08-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
72	imp-1062	2026-08-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
73	imp-1063	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
74	imp-1064	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
75	imp-1065	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
76	imp-1066	2026-07-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
77	imp-1067	2026-07-23 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
78	imp-1068	2026-07-31 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
79	imp-1069	2026-07-09 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
80	imp-107	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
81	imp-1070	2026-07-27 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
82	imp-1071	2026-08-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
83	imp-1072	2026-07-27 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
84	imp-1073	2026-07-29 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
85	imp-1074	2026-07-31 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
86	imp-1075	2026-08-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
87	imp-1076	2026-08-03 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
88	imp-1077	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
89	imp-1078	2026-08-03 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
90	imp-1079	2026-07-29 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
91	imp-108	2026-06-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
92	imp-1080	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
93	imp-1081	2026-07-28 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
94	imp-1082	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
95	imp-1083	2026-08-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
96	imp-1084	2026-08-03 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
97	imp-1085	2026-08-04 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
98	imp-1086	2026-08-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
99	imp-1087	2026-07-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
100	imp-1088	2026-07-31 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
101	imp-1089	2026-07-27 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
102	imp-109	2026-06-02 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
103	imp-1090	2026-07-31 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
104	imp-1091	2026-08-05 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
105	imp-1092	2026-08-05 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
106	imp-1093	2026-08-05 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
107	imp-1094	2026-07-29 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
108	imp-1095	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
109	imp-1096	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
110	imp-1097	2026-08-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
111	imp-1098	2026-07-17 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
112	imp-1099	2026-08-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
113	imp-11	2026-05-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
114	imp-110	2026-06-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
115	imp-1100	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
116	imp-1101	2026-08-04 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
117	imp-1102	2026-08-05 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
118	imp-1103	2026-08-03 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
119	imp-1104	2026-08-03 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
120	imp-1105	2026-08-06 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
121	imp-1106	2026-08-06 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
122	imp-1107	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
123	imp-1108	2026-08-06 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
124	imp-1109	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
125	imp-111	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
126	imp-1110	2026-07-18 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
127	imp-1111	2026-07-31 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
128	imp-1112	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
129	imp-1113	2026-08-06 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
130	imp-1114	2026-07-18 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
131	imp-1115	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
132	imp-1116	2026-08-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
133	imp-1117	2026-08-08 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
134	imp-1118	2026-07-18 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
135	imp-1119	2026-07-18 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
136	imp-112	2026-06-03 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
137	imp-1120	2026-08-08 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
138	imp-1121	2026-08-03 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
139	imp-1122	2026-07-18 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
140	imp-1123	2026-08-08 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
141	imp-1124	2026-08-08 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
142	imp-1125	2026-08-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
143	imp-1126	2026-08-08 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
144	imp-1127	2026-08-08 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
145	imp-1128	2026-08-10 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
146	imp-1129	2026-08-05 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
147	imp-113	2026-06-05 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
148	imp-1130	2026-08-10 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
149	imp-1131	2026-08-03 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
150	imp-1132	2026-08-10 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
151	imp-1133	2026-07-23 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
152	imp-1134	2026-08-08 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
153	imp-1135	2026-07-28 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
154	imp-1136	2026-08-06 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
155	imp-1137	2026-08-08 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
156	imp-1138	2026-08-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
157	imp-1139	2026-08-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
158	imp-114	2026-06-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
159	imp-1140	2026-08-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
160	imp-1141	2026-08-10 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
161	imp-1142	2026-08-06 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
162	imp-1143	2026-08-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
163	imp-1144	2026-08-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
164	imp-1145	2026-08-11 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
165	imp-1146	2026-08-07 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
166	imp-1147	2026-07-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
167	imp-1148	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
168	imp-1149	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
169	imp-115	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
170	imp-1150	2026-08-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
171	imp-1151	2026-08-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
172	imp-1152	2026-08-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
173	imp-1153	2026-08-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
174	imp-1154	2026-08-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
175	imp-1155	2026-07-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
176	imp-1156	2026-08-04 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
177	imp-1157	2026-08-04 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
178	imp-1158	2026-08-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
179	imp-1159	2026-08-10 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
180	imp-116	2026-05-16 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
181	imp-1160	2026-08-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
182	imp-1161	2026-08-11 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
183	imp-1162	2026-08-13 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
184	imp-1163	2026-08-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
185	imp-1164	2026-08-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
186	imp-1165	2026-07-21 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
187	imp-1166	2026-07-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
188	imp-1167	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
189	imp-1168	2026-07-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
190	imp-1169	2026-08-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
191	imp-117	2026-05-30 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
192	imp-1170	2026-08-14 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
193	imp-1171	2026-07-27 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
194	imp-1172	2026-07-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
195	imp-1173	2026-08-12 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
196	imp-1174	2026-08-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
197	imp-1175	2026-08-14 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
198	imp-1176	2026-08-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
199	imp-1177	2026-08-14 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
200	imp-1178	2026-08-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
201	imp-1179	2026-08-14 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
202	imp-118	2026-05-30 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
203	imp-1180	2026-08-14 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
204	imp-1181	2026-08-14 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
205	imp-1182	2026-07-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
206	imp-1183	2026-07-24 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
207	imp-1184	2026-07-16 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
208	imp-1185	2026-08-15 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
209	imp-1186	2026-07-25 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
210	imp-1187	2026-08-15 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
211	imp-1188	2026-08-05 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
212	imp-1189	2026-08-15 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
213	imp-119	2026-06-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
214	imp-1190	2026-08-15 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
215	imp-1191	2026-08-15 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
216	imp-1192	2026-08-15 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
217	imp-1193	2026-08-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
218	imp-1194	2026-08-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
219	imp-1195	2026-08-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
220	imp-1196	2026-08-15 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
221	imp-1197	2026-07-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
222	imp-1198	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
223	imp-1199	2026-08-14 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
224	imp-12	2026-06-01 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
225	imp-120	2026-06-05 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
226	imp-1200	2026-08-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
227	imp-1201	2026-08-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
228	imp-1202	2026-08-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
229	imp-1203	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
230	imp-1204	2026-08-12 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
231	imp-1205	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
232	imp-1206	2026-08-18 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
233	imp-1207	2026-08-18 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
234	imp-1208	2026-08-18 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
235	imp-1209	2026-08-12 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
236	imp-121	2026-05-29 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
237	imp-1210	2026-08-05 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
238	imp-1211	2026-07-29 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
239	imp-1212	2026-07-29 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
240	imp-1213	2026-08-06 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
241	imp-1214	2026-08-19 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
242	imp-1215	2026-08-19 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
243	imp-1216	2026-08-19 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
244	imp-1217	2026-08-19 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
245	imp-1218	2026-08-15 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
246	imp-1219	2026-08-18 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
247	imp-122	2026-05-15 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
248	imp-1220	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
249	imp-1221	2026-07-30 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
250	imp-1222	2026-08-19 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
251	imp-1223	2026-08-20 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
252	imp-1224	2026-08-20 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
253	imp-1225	2026-08-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
254	imp-1226	2026-08-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
255	imp-1227	2026-08-08 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
256	imp-1228	2026-08-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
257	imp-1229	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
258	imp-123	2026-06-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
259	imp-1230	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
260	imp-1231	2026-07-27 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
261	imp-1232	2026-07-27 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
262	imp-1233	2026-08-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
263	imp-1234	2026-08-20 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
264	imp-1235	2026-08-18 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
265	imp-1236	2026-07-23 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
266	imp-1237	2026-08-06 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
267	imp-1238	2026-08-21 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
268	imp-1239	2026-07-22 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
269	imp-124	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
270	imp-1240	2026-08-19 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
271	imp-1241	2026-07-22 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
272	imp-1242	2026-07-29 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
273	imp-1243	2026-08-13 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
274	imp-1244	2026-08-21 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
275	imp-1245	2026-08-21 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
276	imp-1246	2026-07-31 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
277	imp-1247	2026-08-21 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
278	imp-1248	2026-08-21 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
279	imp-1249	2026-08-21 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
280	imp-125	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
281	imp-1250	2026-08-05 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
282	imp-1251	2026-08-06 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
283	imp-1252	2026-08-18 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
284	imp-1253	2026-07-25 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
285	imp-1254	2026-08-21 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
286	imp-1255	2026-07-25 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
287	imp-1256	2026-07-25 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
288	imp-1257	2026-07-31 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
289	imp-1258	2026-07-27 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
290	imp-1259	2026-08-22 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
291	imp-126	2026-05-16 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
292	imp-1260	2026-08-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
293	imp-1261	2026-08-20 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
294	imp-1262	2026-08-22 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
295	imp-1263	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
296	imp-1264	2026-08-21 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
297	imp-1265	2026-08-19 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
298	imp-1266	2026-08-18 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
299	imp-1267	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
300	imp-1268	2026-08-20 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
301	imp-1269	2026-08-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
302	imp-127	2026-05-30 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
303	imp-1270	2026-08-20 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
304	imp-1271	2026-08-20 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
305	imp-1272	2026-08-20 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
306	imp-1273	2026-07-27 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
307	imp-1274	2026-08-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
308	imp-1275	2026-08-25 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
309	imp-1276	2026-08-25 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
310	imp-1277	2026-08-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
311	imp-1278	2026-08-05 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
312	imp-1279	2026-08-24 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
313	imp-128	2026-06-05 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
314	imp-1280	2026-08-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
315	imp-1281	2026-08-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
316	imp-1282	2026-08-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
317	imp-1283	2026-08-06 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
318	imp-1284	2026-08-27 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
319	imp-1285	2026-07-27 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
320	imp-1286	2026-08-06 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
321	imp-1287	2026-08-06 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
322	imp-1288	2026-08-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
323	imp-1289	2026-08-26 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
324	imp-129	2026-05-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
325	imp-1290	2026-08-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
326	imp-1291	2026-08-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
327	imp-1292	2026-08-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
328	imp-1293	2026-08-26 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
424	imp-19	2026-05-07 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
329	imp-1294	2026-08-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
330	imp-1295	2026-08-26 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
331	imp-1296	2026-08-26 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
332	imp-1297	2026-08-26 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
333	imp-1298	2026-07-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
334	imp-1299	2026-07-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
335	imp-13	2026-05-08 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
336	imp-130	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
337	imp-1300	2026-07-18 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
338	imp-1301	2026-07-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
339	imp-1302	2026-07-21 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
340	imp-1303	2026-08-27 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
341	imp-1304	2026-08-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
342	imp-1305	2026-08-28 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
343	imp-1306	2026-08-28 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
344	imp-1307	2026-07-28 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
345	imp-1308	2026-08-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
346	imp-1309	2026-08-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
347	imp-131	2026-06-05 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
348	imp-1310	2026-08-27 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
349	imp-1311	2026-08-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
350	imp-1312	2026-08-27 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
351	imp-1313	2026-08-27 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
352	imp-1314	2026-07-23 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
353	imp-1315	2026-08-26 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
354	imp-1316	2026-08-29 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
355	imp-1317	2026-08-29 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
356	imp-1318	2026-08-27 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
357	imp-1319	2026-08-27 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
358	imp-132	2026-05-15 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
359	imp-1320	2026-08-31 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
360	imp-1321	2026-08-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
361	imp-1322	2026-08-31 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
362	imp-133	2026-05-19 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
363	imp-134	2026-05-19 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
364	imp-135	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
365	imp-136	2026-05-19 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
366	imp-137	2026-05-19 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
367	imp-138	2026-06-09 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
368	imp-139	2026-06-09 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
369	imp-14	2026-05-07 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
370	imp-140	2026-05-28 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
371	imp-141	2026-06-09 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
372	imp-142	2026-06-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
373	imp-143	2026-06-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
374	imp-144	2026-06-09 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
375	imp-145	2026-06-03 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
376	imp-146	2026-06-03 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
377	imp-147	2026-06-03 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
378	imp-148	2026-05-20 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
379	imp-149	2026-06-05 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
380	imp-15	2026-06-03 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
381	imp-150	2026-06-09 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
382	imp-151	2026-06-04 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
383	imp-152	2026-06-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
384	imp-153	2026-06-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
385	imp-154	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
386	imp-155	2026-05-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
387	imp-156	2026-06-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
388	imp-157	2026-06-10 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
389	imp-158	2026-06-04 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
390	imp-159	2026-06-03 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
391	imp-16	2026-05-07 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
392	imp-160	2026-06-04 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
393	imp-161	2026-06-04 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
394	imp-162	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
395	imp-163	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
396	imp-164	2026-06-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
397	imp-165	2026-06-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
398	imp-166	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
399	imp-167	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
400	imp-168	2026-06-10 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
401	imp-169	2026-06-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
402	imp-17	2026-05-07 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
403	imp-170	2026-06-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
404	imp-171	2026-06-04 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
405	imp-172	2026-06-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
406	imp-173	2026-06-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
407	imp-174	2026-06-02 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
408	imp-175	2026-06-11 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
409	imp-176	2026-06-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
410	imp-177	2026-06-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
411	imp-178	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
412	imp-179	2026-06-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
413	imp-18	2026-06-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
414	imp-180	2026-06-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
415	imp-181	2026-06-04 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
416	imp-182	2026-06-09 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
417	imp-183	2026-06-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
418	imp-184	2026-06-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
419	imp-185	2026-05-21 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
420	imp-186	2026-06-10 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
421	imp-187	2026-06-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
422	imp-188	2026-06-04 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
423	imp-189	2026-06-03 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
425	imp-190	2026-06-04 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
426	imp-191	2026-06-04 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
427	imp-192	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
428	imp-193	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
429	imp-194	2026-06-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
430	imp-195	2026-06-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
431	imp-196	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
432	imp-197	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
433	imp-198	2026-06-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
434	imp-199	2026-05-20 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
435	imp-2	2026-05-21 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
436	imp-20	2026-05-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
437	imp-200	2026-06-11 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
438	imp-201	2026-06-10 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
439	imp-202	2026-06-11 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
440	imp-203	2026-06-05 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
441	imp-204	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
442	imp-205	2026-05-20 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
443	imp-206	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
444	imp-207	2026-06-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
445	imp-208	2026-05-16 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
446	imp-209	2026-06-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
447	imp-21	2026-06-04 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
448	imp-210	2026-05-23 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
449	imp-211	2026-05-23 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
450	imp-212	2026-06-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
451	imp-213	2026-06-12 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
452	imp-214	2026-05-19 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
453	imp-215	2026-06-10 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
454	imp-216	2026-06-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
455	imp-217	2026-06-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
456	imp-218	2026-06-04 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
457	imp-219	2026-06-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
458	imp-22	2026-05-07 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
459	imp-220	2026-06-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
460	imp-221	2026-06-02 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
461	imp-222	2026-06-11 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
462	imp-223	2026-06-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
463	imp-224	2026-06-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
464	imp-225	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
465	imp-226	2026-06-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
466	imp-227	2026-06-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
467	imp-228	2026-06-04 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
468	imp-229	2026-06-09 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
469	imp-23	2026-06-04 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
470	imp-230	2026-06-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
471	imp-231	2026-06-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
472	imp-232	2026-05-21 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
473	imp-233	2026-06-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
474	imp-234	2026-06-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
475	imp-235	2026-06-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
476	imp-236	2026-06-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
477	imp-237	2026-06-11 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
478	imp-238	2026-06-11 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
479	imp-239	2026-06-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
480	imp-24	2026-05-07 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
481	imp-240	2026-06-11 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
482	imp-241	2026-06-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
483	imp-242	2026-05-22 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
484	imp-243	2026-06-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
485	imp-244	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
486	imp-245	2026-06-13 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
487	imp-246	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
488	imp-247	2026-06-06 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
489	imp-248	2026-05-22 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
490	imp-249	2026-05-23 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
491	imp-25	2026-06-04 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
492	imp-250	2026-05-23 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
493	imp-251	2026-06-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
494	imp-252	2026-05-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
495	imp-253	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
496	imp-254	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
497	imp-255	2026-05-29 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
498	imp-256	2026-06-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
499	imp-257	2026-06-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
500	imp-258	2026-06-13 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
501	imp-259	2026-06-13 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
502	imp-26	2026-05-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
503	imp-260	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
504	imp-261	2026-06-06 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
505	imp-262	2026-05-26 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
506	imp-263	2026-05-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
507	imp-264	2026-06-12 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
508	imp-265	2026-05-21 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
509	imp-266	2026-05-26 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
510	imp-267	2026-05-26 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
511	imp-268	2026-06-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
512	imp-269	2026-06-16 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
513	imp-27	2026-05-25 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
514	imp-270	2026-06-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
515	imp-271	2026-06-16 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
516	imp-272	2026-06-12 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
517	imp-273	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
518	imp-274	2026-06-10 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
519	imp-275	2026-06-01 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
520	imp-276	2026-06-17 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
521	imp-277	2026-06-11 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
522	imp-278	2026-06-16 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
523	imp-279	2026-06-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
524	imp-28	2026-05-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
525	imp-280	2026-06-16 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
526	imp-281	2026-05-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
527	imp-282	2026-06-09 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
528	imp-283	2026-06-09 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
529	imp-284	2026-06-17 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
530	imp-285	2026-05-25 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
531	imp-286	2026-06-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
532	imp-287	2026-06-12 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
533	imp-288	2026-06-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
534	imp-289	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
535	imp-29	2026-06-01 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
536	imp-290	2026-06-17 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
537	imp-291	2026-05-22 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
538	imp-292	2026-06-12 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
539	imp-293	2026-06-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
540	imp-294	2026-06-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
541	imp-295	2026-06-13 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
542	imp-296	2026-06-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
543	imp-297	2026-06-01 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
544	imp-298	2026-06-01 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
546	imp-3	2026-05-22 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
547	imp-30	2026-05-08 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
548	imp-300	2026-06-04 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
549	imp-301	2026-06-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
550	imp-302	2026-06-04 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
551	imp-303	2026-06-18 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
552	imp-304	2026-06-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
553	imp-305	2026-06-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
554	imp-306	2026-05-25 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
555	imp-307	2026-06-18 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
556	imp-308	2026-05-21 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
557	imp-309	2026-05-29 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
558	imp-31	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
559	imp-310	2026-06-18 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
560	imp-311	2026-06-17 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
561	imp-312	2026-06-19 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
562	imp-313	2026-05-28 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
563	imp-314	2026-06-12 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
564	imp-315	2026-06-19 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
565	imp-316	2026-06-19 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
566	imp-317	2026-06-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
567	imp-318	2026-06-19 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
568	imp-319	2026-06-18 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
569	imp-32	2026-06-03 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
570	imp-320	2026-05-25 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
571	imp-321	2026-06-18 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
572	imp-322	2026-05-25 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
573	imp-323	2026-06-18 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
574	imp-324	2026-06-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
575	imp-325	2026-05-11 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
576	imp-326	2026-05-11 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
577	imp-327	2026-06-17 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
578	imp-328	2026-06-20 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
579	imp-329	2026-06-10 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
580	imp-33	2026-05-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
581	imp-330	2026-06-20 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
582	imp-331	2026-06-17 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
583	imp-332	2026-05-25 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
584	imp-333	2026-05-25 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
585	imp-334	2026-06-19 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
586	imp-335	2026-06-13 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
587	imp-336	2026-06-20 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
588	imp-337	2026-06-18 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
589	imp-338	2026-06-18 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
590	imp-339	2026-06-18 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
591	imp-34	2026-06-05 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
592	imp-340	2026-06-18 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
593	imp-341	2026-05-29 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
594	imp-342	2026-06-10 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
595	imp-343	2026-06-20 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
596	imp-344	2026-06-19 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
597	imp-345	2026-06-19 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
598	imp-346	2026-06-12 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
599	imp-347	2026-06-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
600	imp-348	2026-05-29 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
601	imp-349	2026-06-19 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
602	imp-35	2026-05-02 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
603	imp-350	2026-06-10 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
604	imp-351	2026-06-12 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
605	imp-352	2026-05-25 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
606	imp-353	2026-06-19 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
607	imp-354	2026-06-12 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
608	imp-355	2026-06-16 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
609	imp-356	2026-06-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
610	imp-357	2026-06-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
611	imp-358	2026-05-30 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
612	imp-359	2026-06-02 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
613	imp-36	2026-05-02 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
614	imp-360	2026-06-20 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
615	imp-361	2026-06-20 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
616	imp-362	2026-05-30 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
617	imp-363	2026-06-15 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
618	imp-364	2026-05-26 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
619	imp-365	2026-06-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
620	imp-366	2026-06-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
621	imp-367	2026-05-25 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
622	imp-368	2026-05-25 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
623	imp-369	2026-06-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
624	imp-37	2026-05-25 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
625	imp-370	2026-06-17 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
626	imp-371	2026-06-22 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
627	imp-372	2026-06-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
628	imp-373	2026-06-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
629	imp-374	2026-06-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
630	imp-375	2026-05-15 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
631	imp-376	2026-05-26 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
632	imp-377	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
633	imp-378	2026-06-09 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
634	imp-379	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
635	imp-38	2026-05-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
636	imp-380	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
637	imp-381	2026-06-04 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
638	imp-382	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
639	imp-383	2026-05-26 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
640	imp-384	2026-06-04 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
641	imp-385	2026-05-26 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
642	imp-386	2026-06-23 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
643	imp-387	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
644	imp-388	2026-06-04 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
645	imp-389	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
646	imp-39	2026-05-02 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
647	imp-390	2026-06-23 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
648	imp-391	2026-06-23 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
649	imp-392	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
650	imp-393	2026-06-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
651	imp-394	2026-06-23 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
652	imp-395	2026-06-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
653	imp-396	2026-06-12 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
654	imp-397	2026-06-09 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
655	imp-398	2026-06-17 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
656	imp-399	2026-05-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
657	imp-4	2026-05-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
658	imp-40	2026-06-06 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
659	imp-400	2026-05-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
660	imp-401	2026-06-13 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
661	imp-402	2026-06-17 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
662	imp-403	2026-06-05 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
663	imp-404	2026-06-05 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
664	imp-405	2026-06-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
665	imp-406	2026-06-16 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
666	imp-407	2026-06-22 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
667	imp-408	2026-06-24 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
668	imp-409	2026-06-09 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
669	imp-41	2026-06-01 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
670	imp-410	2026-06-22 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
671	imp-411	2026-06-09 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
672	imp-412	2026-05-29 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
673	imp-413	2026-06-23 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
674	imp-414	2026-06-23 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
675	imp-415	2026-06-22 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
676	imp-416	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
677	imp-417	2026-05-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
678	imp-418	2026-06-19 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
679	imp-419	2026-06-22 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
680	imp-42	2026-06-01 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
681	imp-420	2026-06-22 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
682	imp-421	2026-06-22 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
683	imp-422	2026-06-23 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
684	imp-423	2026-06-24 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
685	imp-424	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
686	imp-425	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
687	imp-426	2026-06-22 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
688	imp-427	2026-06-25 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
689	imp-428	2026-06-25 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
690	imp-429	2026-05-27 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
691	imp-43	2026-05-02 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
692	imp-430	2026-06-04 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
693	imp-431	2026-06-12 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
694	imp-432	2026-06-12 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
695	imp-433	2026-06-25 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
696	imp-434	2026-06-26 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
697	imp-435	2026-06-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
698	imp-436	2026-06-03 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
699	imp-437	2026-06-02 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
700	imp-438	2026-06-22 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
701	imp-439	2026-06-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
702	imp-44	2026-05-29 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
703	imp-440	2026-06-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
704	imp-441	2026-06-03 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
705	imp-442	2026-06-25 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
706	imp-443	2026-06-17 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
707	imp-444	2026-06-19 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
708	imp-445	2026-06-17 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
709	imp-446	2026-06-17 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
710	imp-447	2026-06-18 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
711	imp-448	2026-06-18 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
712	imp-449	2026-06-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
713	imp-45	2026-06-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
714	imp-450	2026-06-11 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
715	imp-451	2026-06-10 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
716	imp-452	2026-06-18 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
717	imp-453	2026-06-18 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
718	imp-454	2026-06-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
719	imp-455	2026-06-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
720	imp-456	2026-06-25 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
721	imp-457	2026-06-19 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
722	imp-458	2026-05-22 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
723	imp-459	2026-05-22 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
724	imp-46	2026-06-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
725	imp-460	2026-06-04 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
726	imp-461	2026-06-26 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
727	imp-462	2026-06-26 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
728	imp-463	2026-06-26 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
729	imp-464	2026-06-05 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
730	imp-465	2026-06-26 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
731	imp-466	2026-06-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
732	imp-467	2026-06-19 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
733	imp-468	2026-06-22 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
734	imp-469	2026-06-22 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
735	imp-47	2026-05-25 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
736	imp-470	2026-06-22 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
737	imp-471	2026-06-24 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
738	imp-472	2026-06-24 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
739	imp-473	2026-05-16 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
740	imp-474	2026-05-16 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
741	imp-475	2026-06-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
742	imp-476	2026-06-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
743	imp-477	2026-06-26 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
744	imp-478	2026-06-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
745	imp-479	2026-06-06 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
746	imp-48	2026-05-14 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
747	imp-480	2026-06-27 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
748	imp-481	2026-05-23 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
749	imp-482	2026-05-30 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
750	imp-483	2026-05-30 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
751	imp-484	2026-06-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
752	imp-485	2026-06-22 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
753	imp-486	2026-06-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
754	imp-487	2026-05-25 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
755	imp-488	2026-05-25 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
756	imp-489	2026-06-04 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
757	imp-49	2026-05-13 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
758	imp-490	2026-06-25 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
759	imp-491	2026-06-25 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
760	imp-492	2026-06-30 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
761	imp-493	2026-06-30 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
762	imp-494	2026-06-30 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
763	imp-495	2026-06-30 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
764	imp-496	2026-06-09 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
765	imp-497	2026-06-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
766	imp-498	2026-05-13 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
767	imp-499	2026-05-13 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
768	imp-5	2026-05-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
769	imp-50	2026-06-09 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
770	imp-500	2026-06-09 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
771	imp-501	2026-06-25 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
772	imp-502	2026-06-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
773	imp-503	2026-06-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
774	imp-504	2026-06-29 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
775	imp-505	2026-06-30 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
776	imp-506	2026-05-25 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
777	imp-507	2026-05-26 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
778	imp-508	2026-06-10 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
779	imp-509	2026-06-22 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
780	imp-51	2026-06-09 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
781	imp-510	2026-07-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
782	imp-511	2026-07-01 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
783	imp-512	2026-07-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
784	imp-513	2026-07-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
785	imp-514	2026-06-03 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
786	imp-515	2026-06-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
787	imp-516	2026-07-02 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
788	imp-517	2026-07-01 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
789	imp-518	2026-07-01 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
790	imp-519	2026-06-12 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
791	imp-52	2026-06-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
792	imp-520	2026-05-29 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
793	imp-521	2026-05-29 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
794	imp-522	2026-06-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
795	imp-523	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
796	imp-524	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
797	imp-525	2026-07-02 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
798	imp-526	2026-07-02 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
799	imp-527	2026-07-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
800	imp-528	2026-07-03 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
801	imp-529	2026-06-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
802	imp-53	2026-05-30 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
803	imp-530	2026-06-13 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
804	imp-531	2026-06-13 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
805	imp-532	2026-07-03 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
806	imp-533	2026-07-04 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
807	imp-534	2026-07-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
808	imp-535	2026-07-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
809	imp-536	2026-05-30 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
810	imp-537	2026-05-30 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
811	imp-538	2026-07-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
812	imp-539	2026-05-28 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
813	imp-54	2026-05-27 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
814	imp-540	2026-05-28 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
815	imp-541	2026-06-17 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
816	imp-542	2026-07-07 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
817	imp-543	2026-06-04 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
818	imp-544	2026-07-07 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
819	imp-545	2026-06-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
820	imp-546	2026-06-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
821	imp-547	2026-06-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
822	imp-548	2026-06-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
823	imp-549	2026-07-02 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
824	imp-55	2026-06-01 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
825	imp-550	2026-07-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
826	imp-551	2026-06-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
827	imp-552	2026-06-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
828	imp-553	2026-07-04 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
829	imp-554	2026-07-06 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
830	imp-555	2026-07-06 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
831	imp-556	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
832	imp-557	2026-07-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
833	imp-558	2026-07-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
834	imp-559	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
835	imp-56	2026-06-01 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
836	imp-560	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
837	imp-561	2026-07-03 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
838	imp-562	2026-06-05 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
839	imp-563	2026-06-19 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
840	imp-564	2026-06-19 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
841	imp-565	2026-06-19 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
842	imp-566	2026-06-30 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
843	imp-567	2026-06-16 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
844	imp-568	2026-07-09 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
845	imp-569	2026-07-09 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
846	imp-57	2026-05-25 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
847	imp-570	2026-06-19 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
848	imp-571	2026-07-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
849	imp-572	2026-06-17 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
850	imp-573	2026-06-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
851	imp-574	2026-07-08 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
852	imp-575	2026-07-02 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
853	imp-576	2026-06-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
854	imp-577	2026-06-20 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
855	imp-578	2026-07-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
856	imp-579	2026-07-10 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
857	imp-58	2026-05-29 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
858	imp-580	2026-07-02 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
859	imp-581	2026-06-19 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
860	imp-582	2026-07-14 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
861	imp-583	2026-07-14 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
862	imp-584	2026-07-14 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
863	imp-585	2026-06-12 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
864	imp-586	2026-07-10 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
865	imp-587	2026-07-10 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
866	imp-588	2026-07-15 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
867	imp-589	2026-07-11 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
868	imp-59	2026-05-31 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
869	imp-590	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
870	imp-591	2026-07-15 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
871	imp-592	2026-07-15 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
872	imp-593	2026-07-15 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
873	imp-594	2026-07-15 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
874	imp-595	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
875	imp-596	2026-07-09 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
876	imp-597	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
877	imp-598	2026-07-15 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
878	imp-599	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
879	imp-6	2026-06-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
880	imp-60	2026-06-01 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
881	imp-600	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
882	imp-601	2026-07-14 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
883	imp-602	2026-06-10 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
884	imp-603	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
885	imp-604	2026-07-10 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
886	imp-605	2026-07-14 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
887	imp-606	2026-07-15 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
888	imp-607	2026-07-16 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
889	imp-608	2026-07-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
890	imp-609	2026-07-15 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
891	imp-61	2026-05-21 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
892	imp-610	2026-07-09 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
893	imp-611	2026-07-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
894	imp-612	2026-07-14 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
895	imp-613	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
896	imp-614	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
897	imp-615	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
898	imp-616	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
899	imp-617	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
900	imp-618	2026-07-03 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
901	imp-619	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
902	imp-62	2026-06-01 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
903	imp-620	2026-07-14 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
904	imp-621	2026-07-15 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
905	imp-622	2026-07-18 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
906	imp-623	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
907	imp-624	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
908	imp-625	2026-07-14 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
909	imp-626	2026-06-27 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
910	imp-627	2026-07-15 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
911	imp-628	2026-07-17 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
912	imp-629	2026-07-18 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
913	imp-63	2026-06-01 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
914	imp-630	2026-07-17 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
915	imp-631	2026-07-18 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
916	imp-632	2026-07-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
917	imp-633	2026-07-16 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
918	imp-634	2026-06-24 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
919	imp-635	2026-07-18 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
920	imp-636	2026-07-01 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
921	imp-637	2026-06-24 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
922	imp-638	2026-06-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
923	imp-639	2026-07-18 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
924	imp-64	2026-06-01 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
925	imp-640	2026-07-18 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
926	imp-641	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
927	imp-642	2026-07-02 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
928	imp-643	2026-07-03 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
929	imp-644	2026-06-26 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
930	imp-645	2026-06-30 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
931	imp-646	2026-07-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
932	imp-647	2026-05-29 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
933	imp-648	2026-06-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
934	imp-649	2026-06-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
935	imp-65	2026-06-01 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
936	imp-650	2026-07-07 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
937	imp-651	2026-06-30 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
938	imp-652	2026-06-30 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
939	imp-653	2026-06-30 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
940	imp-654	2026-06-17 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
941	imp-655	2026-06-19 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
942	imp-656	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
943	imp-657	2026-07-18 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
944	imp-658	2026-07-21 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
945	imp-659	2026-07-27 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
946	imp-66	2026-05-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
947	imp-660	2026-07-27 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
948	imp-661	2026-06-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
949	imp-662	2026-07-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
950	imp-663	2026-07-23 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
951	imp-664	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
952	imp-665	2026-06-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
953	imp-666	2026-06-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
954	imp-667	2026-07-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
955	imp-668	2026-06-30 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
956	imp-669	2026-07-01 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
957	imp-67	2026-06-01 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
958	imp-670	2026-06-25 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
959	imp-671	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
960	imp-672	2026-06-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
961	imp-673	2026-06-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
962	imp-674	2026-06-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
963	imp-675	2026-06-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
964	imp-676	2026-07-02 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
965	imp-677	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
966	imp-678	2026-06-30 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
967	imp-679	2026-06-30 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
968	imp-68	2026-06-01 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
969	imp-680	2026-06-29 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
970	imp-681	2026-06-29 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
971	imp-682	2026-07-02 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
972	imp-683	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
973	imp-684	2026-06-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
974	imp-685	2026-06-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
975	imp-686	2026-06-29 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
976	imp-687	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
977	imp-688	2026-07-02 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
978	imp-689	2026-06-29 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
979	imp-69	2026-05-30 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
980	imp-690	2026-06-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
981	imp-691	2026-06-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
982	imp-692	2026-06-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
983	imp-693	2026-07-02 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
984	imp-694	2026-07-02 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
985	imp-695	2026-07-02 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
986	imp-696	2026-07-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
987	imp-697	2026-06-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
988	imp-698	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
989	imp-699	2026-07-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
990	imp-7	2026-05-13 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
991	imp-70	2026-05-30 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
992	imp-700	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
993	imp-701	2026-06-25 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
994	imp-702	2026-06-22 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
995	imp-703	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
996	imp-704	2026-07-02 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
997	imp-705	2026-06-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
998	imp-706	2026-06-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
999	imp-707	2026-07-02 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1000	imp-708	2026-07-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1001	imp-709	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1002	imp-71	2026-05-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
1003	imp-710	2026-07-04 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1004	imp-711	2026-06-18 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1005	imp-712	2026-06-20 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1006	imp-713	2026-06-26 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1007	imp-714	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1008	imp-715	2026-07-02 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1009	imp-716	2026-07-06 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1010	imp-717	2026-07-06 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1011	imp-718	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1012	imp-719	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1013	imp-72	2026-05-30 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1014	imp-720	2026-07-01 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1015	imp-721	2026-07-01 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1016	imp-722	2026-07-06 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1017	imp-723	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1018	imp-724	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1019	imp-725	2026-07-01 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1020	imp-726	2026-07-01 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1021	imp-727	2026-07-06 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1022	imp-728	2026-07-03 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1023	imp-729	2026-07-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1024	imp-73	2026-05-29 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1025	imp-730	2026-07-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1026	imp-731	2026-06-17 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1027	imp-732	2026-07-07 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1028	imp-733	2026-06-16 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1029	imp-734	2026-06-16 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1030	imp-735	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1031	imp-736	2026-07-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1032	imp-737	2026-06-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1033	imp-738	2026-07-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1034	imp-739	2026-07-07 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1035	imp-74	2026-06-01 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1036	imp-740	2026-07-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1037	imp-741	2026-07-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1038	imp-742	2026-07-09 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1039	imp-743	2026-07-09 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1040	imp-744	2026-07-09 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1041	imp-745	2026-07-08 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1042	imp-746	2026-07-04 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1043	imp-747	2026-07-09 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1044	imp-748	2026-06-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1045	imp-749	2026-06-20 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1046	imp-75	2026-05-26 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1047	imp-750	2026-07-09 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1048	imp-751	2026-07-07 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
1049	imp-752	2026-07-07 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
1050	imp-753	2026-07-05 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1051	imp-754	2026-06-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1052	imp-755	2026-07-08 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1053	imp-756	2026-06-16 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1054	imp-757	2026-06-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1055	imp-758	2026-07-09 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1056	imp-759	2026-07-08 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1057	imp-76	2026-05-27 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1058	imp-760	2026-06-19 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1059	imp-761	2026-06-19 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1060	imp-762	2026-06-18 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1061	imp-763	2026-07-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1062	imp-764	2026-07-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1063	imp-765	2026-06-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1064	imp-766	2026-07-07 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1065	imp-767	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1066	imp-768	2026-06-11 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1067	imp-769	2026-07-04 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1068	imp-77	2026-05-27 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1069	imp-770	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1070	imp-771	2026-07-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1071	imp-772	2026-07-04 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1072	imp-773	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1073	imp-774	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1074	imp-775	2026-07-09 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1075	imp-776	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1076	imp-777	2026-07-09 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1077	imp-778	2026-07-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1078	imp-779	2026-07-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1079	imp-78	2026-05-30 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1080	imp-780	2026-07-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1081	imp-781	2026-07-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1082	imp-782	2026-06-30 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1083	imp-783	2026-06-21 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1084	imp-784	2026-07-08 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1085	imp-785	2026-07-09 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1086	imp-786	2026-07-08 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1087	imp-787	2026-07-08 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1088	imp-788	2026-07-07 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1089	imp-789	2026-06-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1090	imp-79	2026-05-30 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1091	imp-790	2026-07-14 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1092	imp-791	2026-07-14 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1093	imp-792	2026-07-14 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1094	imp-793	2026-07-08 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1095	imp-794	2026-07-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1096	imp-795	2026-07-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1097	imp-796	2026-06-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1098	imp-797	2026-07-14 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1099	imp-798	2026-07-14 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1100	imp-799	2026-06-17 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1101	imp-8	2026-06-02 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1102	imp-80	2026-06-01 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1103	imp-800	2026-06-17 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1104	imp-801	2026-07-14 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1105	imp-802	2026-06-17 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1106	imp-803	2026-07-14 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1107	imp-804	2026-06-17 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1108	imp-805	2026-07-15 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1109	imp-806	2026-07-15 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1110	imp-807	2026-07-09 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1111	imp-808	2026-07-08 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1112	imp-809	2026-06-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1113	imp-81	2026-05-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1114	imp-810	2026-07-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1115	imp-811	2026-07-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1116	imp-812	2026-07-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1117	imp-813	2026-07-15 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1118	imp-814	2026-07-15 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1119	imp-815	2026-07-15 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1120	imp-816	2026-07-15 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1121	imp-817	2026-07-15 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1122	imp-818	2026-07-16 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1123	imp-819	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1124	imp-82	2026-05-26 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1125	imp-820	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1126	imp-821	2026-07-15 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1127	imp-822	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1128	imp-823	2026-07-06 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1129	imp-824	2026-07-08 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1130	imp-825	2026-07-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1131	imp-826	2026-06-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
1132	imp-827	2026-07-14 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1133	imp-828	2026-06-18 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1134	imp-829	2026-07-16 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1135	imp-83	2026-06-03 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1136	imp-830	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1137	imp-831	2026-07-14 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1138	imp-832	2026-07-15 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1139	imp-833	2026-07-15 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1140	imp-834	2026-07-11 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1141	imp-835	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1142	imp-836	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1143	imp-837	2026-07-17 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1144	imp-838	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1145	imp-839	2026-07-14 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1146	imp-84	2026-05-27 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1147	imp-840	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
1148	imp-841	2026-06-22 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1149	imp-842	2026-07-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1150	imp-843	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1151	imp-844	2026-07-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1152	imp-845	2026-06-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1153	imp-846	2026-06-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1154	imp-847	2026-07-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1155	imp-848	2026-07-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1156	imp-849	2026-07-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1157	imp-85	2026-05-13 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
1158	imp-850	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1159	imp-851	2026-07-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1160	imp-852	2026-07-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1161	imp-853	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1162	imp-854	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1163	imp-855	2026-06-20 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1164	imp-856	2026-07-14 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1165	imp-857	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1166	imp-858	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1167	imp-859	2026-07-10 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1168	imp-86	2026-06-01 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1169	imp-860	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1170	imp-861	2026-07-15 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1171	imp-862	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1172	imp-863	2026-07-21 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1173	imp-864	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1174	imp-865	2026-07-16 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1175	imp-866	2026-07-16 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1176	imp-867	2026-07-10 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1177	imp-868	2026-07-21 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1178	imp-869	2026-07-01 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1179	imp-87	2026-06-02 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1180	imp-870	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1181	imp-871	2026-06-22 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1182	imp-872	2026-07-22 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1183	imp-873	2026-07-22 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1184	imp-874	2026-07-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1185	imp-875	2026-07-22 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1186	imp-876	2026-07-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1187	imp-877	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1188	imp-878	2026-07-22 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1189	imp-879	2026-07-16 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1190	imp-88	2026-06-02 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-confirmado", "origen": "ADC-08"}
1191	imp-880	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1192	imp-881	2026-06-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1193	imp-882	2026-07-15 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1194	imp-883	2026-07-21 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1195	imp-884	2026-07-23 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1196	imp-885	2026-06-18 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1197	imp-886	2026-07-06 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1198	imp-887	2026-07-14 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1199	imp-888	2026-06-18 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1200	imp-889	2026-07-23 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1201	imp-89	2026-06-02 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1202	imp-890	2026-07-23 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1203	imp-891	2026-07-24 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1204	imp-892	2026-06-17 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1205	imp-893	2026-07-24 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1206	imp-894	2026-07-24 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1207	imp-895	2026-06-26 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1208	imp-896	2026-07-24 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1209	imp-897	2026-07-23 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1210	imp-898	2026-07-18 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1211	imp-899	2026-07-22 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1212	imp-9	2026-06-02 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1213	imp-90	2026-06-02 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1214	imp-900	2026-06-20 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1215	imp-901	2026-07-18 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1216	imp-902	2026-07-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1217	imp-903	2026-06-30 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1218	imp-904	2026-06-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1219	imp-905	2026-06-16 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1220	imp-906	2026-06-20 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1221	imp-907	2026-07-24 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1222	imp-908	2026-07-11 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1223	imp-909	2026-07-24 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1224	imp-91	2026-06-02 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1225	imp-910	2026-07-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1226	imp-911	2026-07-18 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1227	imp-912	2026-07-21 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1228	imp-913	2026-07-21 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-cumplido", "origen": "ADC-08"}
1229	imp-914	2026-07-24 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1230	imp-915	2026-07-26 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1231	imp-916	2026-07-26 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1232	imp-917	2026-07-01 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1233	imp-918	2026-07-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1234	imp-919	2026-07-27 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1235	imp-92	2026-06-01 00:00:00	ASESOR CC 1 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1236	imp-920	2026-07-06 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1237	imp-921	2026-07-08 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1238	imp-922	2026-07-27 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1239	imp-923	2026-06-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1240	imp-924	2026-07-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1241	imp-925	2026-07-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1242	imp-926	2026-07-23 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1243	imp-927	2026-07-24 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1244	imp-928	2026-07-24 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1245	imp-929	2026-06-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1246	imp-93	2026-06-04 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1247	imp-930	2026-07-10 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1248	imp-931	2026-07-28 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1249	imp-932	2026-07-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1250	imp-933	2026-07-28 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1251	imp-934	2026-07-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1252	imp-935	2026-07-01 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1253	imp-936	2026-06-25 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1254	imp-937	2026-06-25 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1255	imp-938	2026-07-01 00:00:00	ASESOR CC 2 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-pendiente", "origen": "ADC-08"}
1256	imp-939	2026-07-21 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1257	imp-94	2026-06-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1258	imp-940	2026-06-22 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1259	imp-941	2026-07-28 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1260	imp-942	2026-07-27 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1261	imp-943	2026-07-24 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1262	imp-944	2026-07-08 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1263	imp-945	2026-07-06 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1264	imp-946	2026-07-06 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1265	imp-947	2026-07-23 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1266	imp-948	2026-06-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1267	imp-949	2026-07-29 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1268	imp-95	2026-06-03 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1269	imp-950	2026-07-27 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1270	imp-951	2026-07-28 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1271	imp-952	2026-06-30 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1272	imp-953	2026-07-30 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1273	imp-954	2026-07-30 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1274	imp-955	2026-07-28 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1275	imp-956	2026-07-29 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1276	imp-957	2026-07-30 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1277	imp-958	2026-07-25 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1278	imp-959	2026-07-25 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1279	imp-96	2026-06-04 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1280	imp-960	2026-07-29 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1281	imp-961	2026-07-28 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1282	imp-962	2026-06-25 00:00:00	TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1283	imp-963	2026-07-28 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1284	imp-964	2026-07-31 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1285	imp-965	2026-07-28 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1286	imp-966	2026-07-31 00:00:00	CJMEDICAL * TESORO  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1287	imp-967	2026-07-04 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1288	imp-968	2026-07-04 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1289	imp-969	2026-07-08 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1290	imp-97	2026-05-30 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1291	imp-970	2026-07-06 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1292	imp-971	2026-07-10 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1293	imp-972	2026-07-10 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1294	imp-973	2026-07-17 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1295	imp-974	2026-06-26 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1296	imp-975	2026-07-07 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1297	imp-976	2026-07-07 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1298	imp-977	2026-07-14 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1299	imp-978	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1300	imp-979	2026-07-14 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1301	imp-98	2026-05-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1302	imp-980	2026-07-17 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1303	imp-981	2026-07-27 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1304	imp-982	2026-07-15 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1305	imp-983	2026-07-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1306	imp-984	2026-07-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1307	imp-985	2026-07-09 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1308	imp-986	2026-07-11 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1309	imp-987	2026-07-17 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1310	imp-988	2026-07-11 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1311	imp-989	2026-07-11 00:00:00	CHICO1  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1312	imp-99	2026-06-03 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-incumplido", "origen": "ADC-08"}
1313	imp-990	2026-07-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1314	imp-991	2026-07-25 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-cancelado", "origen": "ADC-08"}
1315	imp-992	2026-07-18 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1316	imp-993	2026-07-08 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1317	imp-994	2026-07-10 00:00:00	CJMEDICAL * BOGOTA  CATALINA JARMILLO	Recepcionista	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1318	imp-995	2026-08-10 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1319	imp-996	2026-08-03 00:00:00	ASESOR CC 5 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1320	imp-997	2026-08-13 00:00:00	SERVICIO AL CLIENTE  CATALINA JARMILLO	Call Center	importada	{"estado": "est-realizado", "origen": "ADC-08"}
1321	imp-998	2026-08-04 00:00:00	ASESOR CC 3 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1322	imp-999	2026-07-30 00:00:00	ASESOR CC 4 CATALINA JARAMILLO	Call Center	importada	{"estado": "est-reprogramado", "origen": "ADC-08"}
1368	imp-299	2026-09-20 19:24:29.2918		Call Center	creada	{"sede": "sede-cj-medical-el-tesoro", "fecha": "2026-06-18", "estado": "est-realizado", "inicio": "14:00:00", "especialista": "esp-valentina-rivillas-baquero-42"}
\.


--
-- Data for Name: clientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clientes (id, tipo_doc, documento, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, telefono, correo, dia_nac, mes_nac, genero, ciudad, sede_id, tipo_cliente, notas, importado, creado_en, creado_por) FROM stdin;
cli-1000332854	Cédula de Ciudadanía	1000332854	JUAN		ESTEBAN	JIMENEZ	15165917780	JUANES9612@OUTLOOK.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1000441777	Cédula de Ciudadanía	1000441777	SALOMON		ORTIZ		ACTUALIZAR NUMERO	ACTUALIZAR CORREO	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1000461276	Cédula de Ciudadanía	1000461276	MARIA	CAMILA	AVILA	FRANCO	3104910415	CAMILAAVILAFRANCO12@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1000534795	Cédula de Ciudadanía	1000534795	SERGIO		MORENO		ACTUALIZAR NUMERO	ACTUALIZAR CORREO	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1000575719	Cédula de Ciudadanía	1000575719	Stephania		Acosta	Bolívar	315 7260503	stephania.acostabo@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1000655431	Cédula de Ciudadanía	1000655431	MARIA		PAULINA	FLOREZ	3246808479	PAULINAFLOREZG@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1000707166	Cédula de Ciudadanía	1000707166	KAROL		VALENTINA	CASTRO	3118768012	Karolpaul2001@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1000900043	Cédula de Ciudadanía	1000900043	NATALIA		BUSTAMANTE		3106371297	NATABUSTAMANTE27@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1000953384	Cédula de Ciudadanía	1000953384	MARIA		VALENTINA	RICO	3209644476	mvalenrico@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1001077567	Cédula de Ciudadanía	1001077567	MANUELA		PARDO		3134475751	MANUELAPS1D@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1001139336	Cédula de Ciudadanía	1001139336	HEIDY		MARCELA	ZAPATA	3052338036	heidymarcelazapta756@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1001140449	Cédula de Ciudadanía	1001140449	SALOME		MIRA		3052270893	SALOMEMIRAR110@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1001419123	Cédula de Ciudadanía	1001419123	DAYANA		BEDOYA		3165375146	dayanabedoya549@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1001447106	Cédula de Ciudadanía	1001447106	JESSICA		RUA		ACTUALIZAR NUMERO	ACTUALIZAR CORREO	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1001481129	Cédula de Ciudadanía	1001481129	KAREN		PARRA		3107266890	Parramarinkaren@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1001534562	Cédula de Ciudadanía	1001534562	VALERIA		AGUDELO	CARCAMO	3106435677	vagudelocarcamo@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1001588849	Cédula de Ciudadanía	1001588849	EMI		LAURI	VERGARA	3007574444	emivergaraartriaga@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1001854605	Cédula de Ciudadanía	1001854605	SEBASTIAN		CERA		3015959961	SEBASCERA@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1002126952	Cédula de Ciudadanía	1002126952	María		Jimena	Vélez	3209472023	Jimenave456@gmail.com	\N	\N			sede-cj-medical-el-tesoro			t	2026-09-20 00:52:54.234108	
cli-1002558907	Cédula de Ciudadanía	1002558907	ANGIE		TAMAYO		3208618667	Tatis.21v@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1002642363	Cédula de Ciudadanía	1002642363	CAROLINA		TORRES		3122474601	caroltorres0113@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1004997406	Cédula de Ciudadanía	1004997406	PAOLA		LEON		3173796000	angiejl_165@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1004999021	Cédula de Ciudadanía	1004999021	ANDREA		CONDE		3164778572	ANCOL_4@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1006820137	Cédula de Ciudadanía	1006820137	SARA		SOTO		3202339830	sarasotogalvis14@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1007353470	Cédula de Ciudadanía	1007353470	MAIKOL		AHUMADA		3106512519	maikoolahumada@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1007622305	Cédula de Ciudadanía	1007622305	MARIA		ALEJANDRA	HERRERA	ACTUALIZAR NUMERO	ACTUALIZAR CORREO	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1010081806	Cédula de Ciudadanía	1010081806	ANDREA		CARDENAS		3053812436	andrealorenacq@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1010148226	Cédula de Ciudadanía	1010148226	NATALY		NIETO		3164040440	NATHY2991@HOTMAIL.COM	18	3			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1010177070	Cédula de Ciudadanía	1010177070	LIZ		MUÑOZ		3205705964	alexa123321@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1010196637	Cédula de Ciudadanía	1010196637	KATHERINE		MORENO		3223065139	KTMORENOAGUDELO@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1010214230	Cédula de Ciudadanía	1010214230	MARY		FERNANDEZ		3185327251	LYNN.F.LJBO@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1010218251	Cédula de Ciudadanía	1010218251	LORENA		CABAL		3142284642	SANDYLORE2710@HOTMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1011393950	Cédula de Ciudadanía	1011393950	LUNA		LONDOÑO		3108958624	luna.londoñov@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1013612199	Cédula de Ciudadanía	1013612199	ALEJANDRA		GIRALDO		3234423171	alegibo707@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1014305681	Cédula de Ciudadanía	1014305681	VALENTINA		ROJAS		3202158656	valro.99@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1014872117	Cédula de Ciudadanía	1014872117	ISABELLA		HOYOS		3013702690	solanomadrid@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1015395409	Cédula de Ciudadanía	1015395409	PAOLA		NOSSA		3123733263	jenpao42@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1015407135	Cédula de Ciudadanía	1015407135	ANGELICA		CASTELLANOS		3213089593	ANGELICAESPEJOCAATELLANOS@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1015427858	Cédula de Ciudadanía	1015427858	MILENA		DUARTE		3193810542	smilena.duarte@outlook.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1015452061	Cédula de Ciudadanía	1015452061	NANCY		PAOLA	ORTIZ	3233921792	nancyortiz1902@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1015452989	Cédula de Ciudadanía	1015452989	MAYERLY		MONROY		3213824293	Kmaye0304@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1015478534	Cédula de Ciudadanía	1015478534	MARIA		JOSE	TORRES	3012908606	torresruizmariajose@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1016092066	Cédula de Ciudadanía	1016092066	LIZETH		DAHIANA	VALENCIA	3107999830	Lizethvalencia5@hotmail.com	2	2			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1016094687	Cédula de Ciudadanía	1016094687	WENDY		OCHOA		3132621405	WENDYOCHOA25@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1017126454	Cédula de Ciudadanía	1017126454	ANGELA		GARCIA		3103827765	gela369@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1017133484	Cédula de Ciudadanía	1017133484	SARA		CATALINA	ARCILA	3122387800	saraarcila@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1017148290	Cédula de Ciudadanía	1017148290	KARLA	CRISTINA	OBANDO	NARVÁEZ	3187164991	KARLACOBANDO@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1017150439	Cédula de Ciudadanía	1017150439	CAROLINA		ECHAVARRIA		3137672710	echavarriacaro@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1017156452	Cédula de Ciudadanía	1017156452	LAURA		ALEJANDRA	LONDOÑO	3174273755	laureis1829@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1017232776	Cédula de Ciudadanía	1017232776	DANIELA		URIBE		3105043635	Daniuribe2@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1017929180	Cédula de Ciudadanía	1017929180	JERONIMO		ROMAN		3023002331	Jeronimoroman39@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1017932526	Cédula de Ciudadanía	1017932526	MATIAS		PEÑA	LOPEZ	3014608031	MATIAS26709PENA@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1018345520	Cédula de Ciudadanía	1018345520	GINA		HERNANDEZ		3008668461	GINAM_hr@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1018415797	Cédula de Ciudadanía	1018415797	JENIFFER		CORDOBA		3204834865	jennico884@hotmail.com	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1018419501	Cédula de Ciudadanía	1018419501	ANDREA		TOVAR		313 2809197	ACTULIZAR	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1018422925	Cédula de Ciudadanía	1018422925	ALEJANDRA		GONZALEZ		3168147444	Aleja60@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1018447506	Cédula de Ciudadanía	1018447506	DIANA		BARRETO		+573223984154	dianabarreto9@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1018456833	Cédula de Ciudadanía	1018456833	MARIA		GABRIELA	GARCIA	3188754478	GABY26_92@HOTMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1018464161	Cédula de Ciudadanía	1018464161	CAMILA		LOPEZ		3058957973	Camila.lopezlaverde@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1018500681	Cédula de Ciudadanía	1018500681	DANIELA		PEDRAZA		3168292561	pedrazamu@gmail.cm	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1019023831	Cédula de Ciudadanía	1019023831	CATALINA		CUERVO		3006600139	catacg3@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1019029968	Cédula de Ciudadanía	1019029968	Clara		Lemus		3105831050	claralemusg@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1019087089	Cédula de Ciudadanía	1019087089	ANGIE		VIVIANA	MONTAÑEZ	3024506243	angiemonful@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1019111289	Cédula de Ciudadanía	1019111289	ADRIANA		RODRIGUEZ	CARVAJAL	3216802436	ADRIANARODCAR95@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1020404375	Cédula de Ciudadanía	1020404375	YULIANA		MEJIA		3174035138	Yuliana.elyu39@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1020413179	Cédula de Ciudadanía	1020413179	ANNY		MONTAÑO		3008804222	VANEMONTA2010@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1020471361	Cédula de Ciudadanía	1020471361	LAURA		PATIÑO		3042172649	Laurapatino37@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1020493425	Cédula de Ciudadanía	1020493425	MARIANA		MORENO	DUQUE	3206671213	MARIANA.M.DUQUE@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1020715074	Cédula de Ciudadanía	1020715074	MARIA		CAROLINA	BARRAGAN	3165238595	carolinabarragamendez@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1020756814	Cédula de Ciudadanía	1020756814	LIZETTE		BALLESTEROS		3228485783	LIZETTEBALLE@HOTMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1020758898	Cédula de Ciudadanía	1020758898	DIANA		MORENO		3146078289	diana.morenoga2@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1020798300	Cédula de Ciudadanía	1020798300	ANGELA	ASTRID	CASTRO	GONZALEZ	3126063605	castroangela1994@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1021927920	Tarjeta de Identidad	1021927920	MARIA		JOSE	GOMEZ	3005723206	LIGIBO2006@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1022335008	Cédula de Ciudadanía	1022335008	PATRICIA		OJEDA		61403763683	Paty8707@yahoo.es	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1022341860	Cédula de Ciudadanía	1022341860	AMPARO		SALCEDO		3214864144	amparasalcedo23@gmail.com	21	12			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1023916448	Cédula de Ciudadanía	1023916448	ANDREA		GUZMAN		3213499054	aguzman@udca.edu.co	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1024540490	Cédula de Ciudadanía	1024540490	DIANA		ROBAYO		3004754204	DIANAECONOMIA3R@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1024543929	Cédula de Ciudadanía	1024543929	WENDY	VIVIANA	TORRES	CUERVO	3143396283	WENDYVIVIANATORRES8@HOTMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1026251454	Cédula de Ciudadanía	1026251454	ELIZA		NATALIA	GARCIA	3206655443	ELISANATALIA.GARCIA@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1026254692	Cédula de Ciudadanía	1026254692	EUGENIA		OSPINA		3183820786	EUOSPINA31@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1026266784	Cédula de Ciudadanía	1026266784	ANDREA		LEE		3504448743	AMYLI0849@HOTMA.COM	13	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1030593561	Cédula de Ciudadanía	1030593561	MABEL		CAMPO		3208666432	MABEL.CAMPO.G@HOTMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1030603570	Cédula de Ciudadanía	1030603570	YENNI		ALEJANDRA	GOMEZ	3203254510	yennyagomezb@gmail.com	29	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1030613205	Cédula de Ciudadanía	1030613205	Vivian		la	farina	311 5327992	Vivianlafarina@gmail.com	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1032406074	Cédula de Ciudadanía	1032406074	NATALIA		GONZALEZ	CELIS	3183622761	natag_99@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1032418627	Cédula de Ciudadanía	1032418627	MARIA		FERNANDA	NEIRA	3014642703	MAFE_NEIRA58@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1032423777	Cédula de Ciudadanía	1032423777	DIANA		JARAMILLO		3105505046	Dianyjaramillo22@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1032427896	Cédula de Ciudadanía	1032427896	CAROLINA		CUELLAR		3203511923	dcc30@gmail.com	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1032460058	Cédula de Ciudadanía	1032460058	ANGELA		JIMENEZ		3022151980	apjimenezm@unal.edu.co	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1033181939	Cédula de Ciudadanía	1033181939	MARIANA		MORALES	GOMEZ	3022667922	MARIANAMORALES0716@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1033654796	Cédula de Ciudadanía	1033654796	ZORAIDA		GARCIA	RAMIREZ	3014495462	soraidagarcia1995@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1033722369	Cédula de Ciudadanía	1033722369	MAYERLY		ROJAS		3132807231	maye.mr10@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1034294175	Cédula de Ciudadanía	1034294175	JESSICA		GUTIERREZ		3045966433	jessicagutierrezm@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1034991123	Cédula de Ciudadanía	1034991123	ANA	SOFIA	RAMIREZ	GOMEZ	3508521476	MILE4812@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1034993103	Cédula de Ciudadanía	1034993103	MARIA		PAZ	ARISTIZABAL	3113408487	pazaristi23@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1034994995	Cédula de Ciudadanía	1034994995	JUANITA		RESTREPO		3001677634	Pabamos77@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1034995289	Tarjeta de Identidad	1034995289	ADELAIDA		PAUCAR		3014864093	ADELEIDPAU@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1034999825	Cédula de Ciudadanía	1034999825	LUNA		CORREA		3123811846	lunacorr34@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1035438745	Cédula de Ciudadanía	1035438745	ANGELA		ARDILA		3193119778	ANGELAMARIA.ARDILAB97@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1035862006	Cédula de Ciudadanía	1035862006	LIZTHE		YURANI		3126236641	LISNAO-@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1036603493	Cédula de Ciudadanía	1036603493	CRISTINA		VELASQUEZ		3234798016	lanegra_921@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1036607047	Cédula de Ciudadanía	1036607047	DANIELA		CARVAJAL		3113758344	Danielacv16@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1036614057	Cédula de Ciudadanía	1036614057	MARISOL		GOMEZ		3165345580	mgm.8813@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1036620763	Cédula de Ciudadanía	1036620763	SANDRA		HOLGUIN		3147543397	S-AMI-1401@GAMIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1036627141	Cédula de Ciudadanía	1036627141	YTESICA		SARMIENTO		+1908267712	JESS022621@GIMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1036627387	Cédula de Ciudadanía	1036627387	YULIANA		ANDREA	MANCO	3182467106	YULIANAMANCO3@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1036631947	Cédula de Ciudadanía	1036631947	ANA		TATIANA	VELEZ	3142749919	TATIANAVELEZ0606@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1036635136	Cédula de Ciudadanía	1036635136	DEICY		RESTREPO		3206618997	DEICY.RESTREPOS23@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1036648060	Cédula de Ciudadanía	1036648060	JULIANA		ZEA		3046640072	sas.espacioseducativos@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1037570253	Cédula de Ciudadanía	1037570253	LEIDY		LONDOÑO		3226601999	Mile1037@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1037570796	Cédula de Ciudadanía	1037570796	LAURA		FLOREZ		3006466765	FLOREZ123@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1037571876	Cédula de Ciudadanía	1037571876	STEPHANIE		GIESE		3206896925	sgiesec@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1037578944	Cédula de Ciudadanía	1037578944	LAURA		ACOSTA	TOBON	3003717037	LAURAACOSTA0122@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1037591863	Cédula de Ciudadanía	1037591863	SALOME		VILLEGAS		3108035556	salomevillegas@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1037604025	Cédula de Ciudadanía	1037604025	VALENTINA		LONDOÑO		3174030458	valenlondo@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1037604751	Cédula de Ciudadanía	1037604751	DIANA		VARGAS		3006720818	diavargas0613@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1037608047	Cédula de Ciudadanía	1037608047	DANIELA		CARVAJAL		3113758344	Danielacv16@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1037610906	Cédula de Ciudadanía	1037610906	CAMILA		LONDOÑO		3136995955	camila.londono@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1037613328	Cédula de Ciudadanía	1037613328	ANDREA		HOYOS	OSPINA	3117997583	andreh2791@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1037613769	Cédula de Ciudadanía	1037613769	MABEL	ANDREA	SALDARRIAGA	ZAPATA	3136107261	andrea_20.09@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1037620783	Cédula de Ciudadanía	1037620783	Susana		Castillo		301 7903751	susanacastillov@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1037622259	Cédula de Ciudadanía	1037622259	LAURA		DE	BEDOUT	3117720791	cristix92@msn.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1037624943	Cédula de Ciudadanía	1037624943	LUISA		URAN		3164207904	luisauran@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1037634850	Cédula de Ciudadanía	1037634850	SUSANA		MERIZALDE		3002942008	susanamerizaldemaya@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1037635627	Cédula de Ciudadanía	1037635627	ESTEFANIA		CANO		18135397778	ESTEFACANOV@GMAIL.COM	27	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1037644195	Cédula de Ciudadanía	1037644195	DANIELA		MENDEZ		3105994870	daniela.mendezsj@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1037648065	Cédula de Ciudadanía	1037648065	ANII		CARDONA		3104343345	bogotacjmedical@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1037668476	Cédula de Ciudadanía	1037668476	TOMAS		LOAIZA	JIMENEZ	3116491002	loaiza.tomas@gmail.com	23	5			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1037670965	Cédula de Ciudadanía	1037670965	FERNANDA		HERNANDEZ		3104465574	mfernandahz5@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1037671756	Cédula de Ciudadanía	1037671756	MARIA		CAMILA	AGUDELO	3244390126	MARICAM-27@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1038105046	Cédula de Ciudadanía	1038105046	NATALIA		VELASQUEZ		3104952472	NATYFERNANDA288@OUTLOOK.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1038262441	Cédula de Ciudadanía	1038262441	MARIA		ISABEL	ZAPATA	3136884350	MARIAISAZAPATAZ@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1039448466	Cédula de Ciudadanía	1039448466	Carolina		Henao	Ramirez	3137500015	caritohenaoramirez@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1039457628	Cédula de Ciudadanía	1039457628	CAROLINA		MONTOYA		19548737365	carolinamont4@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1040515348	Cédula de Ciudadanía	1040515348	VALENTINA		PEREZ		3015298666	valentinapj@hotmail.es	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1040736835	Cédula de Ciudadanía	1040736835	ALEJANDRA		SIERRA		3003794190	ALEJASIERRA2017@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1041151982	Cédula de Ciudadanía	1041151982	VALENTINA		SUAZA	TORO	3006161080	valen.or99@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1041611004	Cédula de Ciudadanía	1041611004	MARIA		TERESA	ARENAS	3004843946	MARIATERESAARENAS10@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1042771641	Cédula de Ciudadanía	1042771641	CAMILA		CARVAJAL		3017424198	bogotacatalinajaramillo@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1043435034	Cédula de Ciudadanía	1043435034	MADAY		TORRES		ACTUALIZAR NUMERO	ACTUALIZAR CORREO	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1045017321	Cédula de Ciudadanía	1045017321	Leidy		Gómez		3156505203	leididi74@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1045421615	Cédula de Ciudadanía	1045421615	MONICA		MARIN		3113668676	marceor27@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1045755137	Cédula de Ciudadanía	1045755137	VALERIA		RESTREPO		3506015357	RESTREPORIOSVALERIA@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1046666281	Cédula de Ciudadanía	1046666281	CAROLINA		ARENAS		3233663898	MACECA1511@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1046907474	Cédula de Ciudadanía	1046907474	WENDY		CASTAÑO		3104693226	liceth_2190@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1050951071	Cédula de Ciudadanía	1050951071	ELIANA		MARTINEZ		301 2320933	iliamar2402@hotmail.com	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1052389892	Cédula de Ciudadanía	1052389892	JULIAN		MESA		3203254510	TENNYAGOMEZB@GAMAIL.COM	16	2			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1052391724	Cédula de Ciudadanía	1052391724	YINA		ADAME		3204244210	Yinaadame@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1052397670	Cédula de Ciudadanía	1052397670	LAURA		CASTRO		3213078169	lcastro@comdisllantas.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1053330716	Cédula de Ciudadanía	1053330716	NELCY		AVILA		3175634925	nelcy123@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1053789864	Cédula de Ciudadanía	1053789864	JULIANA		LOPEZ		3128710974	JLOPEZV688@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1053811453	Cédula de Ciudadanía	1053811453	VALENTINA		HINCAPIE		3152597437	VALEN7889@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1057710556	Cédula de Ciudadanía	1057710556	LUCI		RIVERA	SANCHEZ	3214648369	LUCIRIVERA90@AICLOUD.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1063144451	Cédula de Ciudadanía	1063144451	JILLIAN		GENES		3001856477	genezperezjillian@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1067951904	Cédula de Ciudadanía	1067951904	VIUNY		PEREZ		3044358300	Viunyrp0314@hotmail.es	\N	\N			sede-cj-medical-el-tesoro			t	2026-09-20 00:52:54.234108	
cli-1075270783	Cédula de Ciudadanía	1075270783	KAROL		GARCIA		3144031802	KAROLGARCIAZ50@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1077034356	Cédula de Ciudadanía	1077034356	RUDDY		MILENA	BARRAGAN	3167571044	rbp.17@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1082856396	Cédula de Ciudadanía	1082856396	ALICIA		PEÑARANDA	FERNANDEZ	3145851028	ALICIAPENARANGAF@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1085277604	Cédula de Ciudadanía	1085277604	MARIA		AZAIN	AYALA	3136203107	Mariazain@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1088304912	Cédula de Ciudadanía	1088304912	PAULA		CARDONA		3007670258	PAULA.CARDONA@TRIARKA.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1090378631	Cédula de Ciudadanía	1090378631	MARIA		ISABEL	VILLAMIZAR	3008302323	maisabelvilla@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1090480034	Cédula de Ciudadanía	1090480034	ANDREINA		CONTRERAS		3158111200	ANDREINA.NINA@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1090493435	Cédula de Ciudadanía	1090493435	MARIA		ELENA	CASTAÑO	3224746842	MARIAELENACASTANOG@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1090547471	Cédula de Ciudadanía	1090547471	OSCAR		MAITA		3137491611	OSACRAMAITA@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1093801735	Cédula de Ciudadanía	1093801735	MARIA		MONICA	OCHOA	3043356278	MONICA8A23@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1094881949	Cédula de Ciudadanía	1094881949	PILAR		JARAMILLO		3212351404	pili_jaramillo@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1094977327	Cédula de Ciudadanía	1094977327	MICHELL		FLOREZ		3104870547	MICHELLFLOREZ0916@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1098757306	Cédula de Ciudadanía	1098757306	PAOLA		GOMEZ		3185920703	PAOLAGOMEZ@YAHOO.ES	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1102799405	Cédula de Ciudadanía	1102799405	MARIA		INES	MERCADO	3112486378	mariaines.mghg@gmail.com	19	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1102840319	Cédula de Ciudadanía	1102840319	KATERINNE		MARTINEZ		3188999479	Kate_martinez0430@hotmail.com	2	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1105693410	Cédula de Ciudadanía	1105693410	ISABELLA		MANOTAS		3153895756	bogotacatalinajaramillo@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1107069165	Cédula de Ciudadanía	1107069165	ISABELLA		GALLEGO		3122599969	gallegoisabella11@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1107072156	Cédula de Ciudadanía	1107072156	JOHANA		MONTENEGRO		3113400024	JoaMontenegro22@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1112776705	Cédula de Ciudadanía	1112776705	MELISSA		CASTRILLON		3168272321	melissa_1706@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1115087263	Cédula de Ciudadanía	1115087263	ANGELINA		VANEGAS		3133909761	ANGEVANENAS24@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1116256148	Cédula de Ciudadanía	1116256148	ANA		ISABEL	GALINDO	3185743689	ANNAISABELGALINDO@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1121825659	Cédula de Ciudadanía	1121825659	LEIDY		MARCELA	ROMERO	3127950721	leidymarcela08@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1121926043	Cédula de Ciudadanía	1121926043	LAURA		GONZALEZ		3246820675	Lauragonzalez14@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1125293826	Cédula de Extranjería	1125293826	YVONNE		GALLON		3117048632	Yvonne_gallon@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1125598288	Cédula de Ciudadanía	1125598288	SALOME		CUETER		3017902858	SOLMECUETER@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1125598715	Tarjeta de Identidad	1125598715	LUANA		CUETER		3007117964	luanacueter@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1125795486	Cédula de Ciudadanía	1125795486	TATIANA		BUERGOS		16096130838	TATIBU1@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1128264708	Cédula de Ciudadanía	1128264708	ALEJANDRA		VILLEGAS	LONDOÑO	3104929551	alejavillegas10@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1128266791	Cédula de Ciudadanía	1128266791	MARIA		CLARA	PEREZ	3103617038	Clarita1708@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1128269414	Cédula de Ciudadanía	1128269414	JULIANA		GIRALDO		3206917696	jgiraldo@refrilogistica.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1128271921	Cédula de Ciudadanía	1128271921	DAVID		PELAEZ		17866436899	danieladiaz0320@yahoo.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1128271946	Cédula de Ciudadanía	1128271946	PATRICIA		HENAO		3002813830	MPHARANGO@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1128273353	Cédula de Ciudadanía	1128273353	MARIA		ANTONIA	SIERR	3202556186	marysierra22@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1128276823	Cédula de Ciudadanía	1128276823	ANA		MARÍA	BOHÓRQUEZ	3136444619	ANA.BOHORQUEZC@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1128397229	Cédula de Ciudadanía	1128397229	DANIELA		LOPERA	MONTOYA	3148114704	DANILAM89@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1128405584	Cédula de Ciudadanía	1128405584	JOHANA		VALENCIA		3113627347	facturacionheavencompany@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1128429628	Cédula de Ciudadanía	1128429628	DIANA		DURANGO		3243586561	Diana.dz@live.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1128438388	Cédula de Ciudadanía	1128438388	NATALIA		ARIAS		3016654415	NATYARIAS_17M@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1128441518	Cédula de Ciudadanía	1128441518	YULIANA	PATRICIA	LOPEZ	METAUTE	3146211058	YULIANALOPEZ92@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1128448142	Cédula de Ciudadanía	1128448142	ANDREA		HENAO		3017382860	Andreahenao@sura.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1128458678	Cédula de Ciudadanía	1128458678	DAHIANA		RESTREPO		3016360333	Dahiana.restrepo@avianca.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1128474994	Cédula de Ciudadanía	1128474994	JULIANA		VELASQUEZ		3046568182	VELAS_JULIANA@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1130620215	Cédula de Ciudadanía	1130620215	LAURA		CAMACHO		3005968090	camacholaura091@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-28561811	Cédula de Ciudadanía	28561811	MARTHA		HEREDIA		3202551403	marheredia3@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1130667990	Cédula de Ciudadanía	1130667990	ANDREA		DURAN		3115720758	ANDREADURAN1113@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1137978165	Cédula de Ciudadanía	1137978165	LUNA		NEGRETTE	RODRIGUEZ	3045937057	carolinarodrigueznegretet@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1141520024	Tarjeta de Identidad	1141520024	ISABELA		VIZCAINO		3138309500	S.GUTIERREZCARRILLO@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1143148111	Cédula de Ciudadanía	1143148111	LEIDY	ESTHER	SUANCHA	URAN	3017205372	llellysuancha7@gmail.com	21	11			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1143337034	Cédula de Ciudadanía	1143337034	LIZETH		MEJIA		3042438993	lmejiaba@gmail.con	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1144134987	Cédula de Ciudadanía	1144134987	LAURA		GALLEGO		3108414527	LD.GALLEGO24@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1151953915	Cédula de Ciudadanía	1151953915	ANDREA		VELASCO		3106704561	ANDREA_0972@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1152188224	Cédula de Ciudadanía	1152188224	MARIXA		ORTEGA		3234565621	LELAORTEGAORTEGA@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1152191791	Cédula de Ciudadanía	1152191791	ESTEFANIA		RUIZ		19144463380	STEFARUIZ2010@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1152192832	Cédula de Ciudadanía	1152192832	MANUELA		BEDOYA	GARCIA	3014376597	MANUELABEGA813@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1152193761	Cédula de Ciudadanía	1152193761	ISABEL		MATURANA		3147467720	ISABEL87MATURANA@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1152199414	Cédula de Ciudadanía	1152199414	MAGALY		LONDOÑO		3107082143	magalonblan_93@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1152211441	Cédula de Ciudadanía	1152211441	MANUELA		ZAPATA		ACTUALIZAR NUMERO	ACTUALIZAR CORREO	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1152226930	Cédula de Ciudadanía	1152226930	MARIA		FERNANDA	OME	3008689101	MFERNANDAOME@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1152442530	Cédula de Ciudadanía	1152442530	DANIELA		DIAZ		17866436899	danieladiaz0320@yahoo.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1152442893	Cédula de Ciudadanía	1152442893	DANIELA		BARRERA		3114139532	bomadabaga30@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1152465203	Cédula de Ciudadanía	1152465203	YULIANA		RUIZ	VELASQUEZ	3226660503	yulianaruiz718@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1192768653	Cédula de Ciudadanía	1192768653	DANIELA		BEDOYA		3219489289	DBTOBAR@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-12022353	Cédula de Ciudadanía	12022353	JESUS		BEJARANO		3206853547	bejaranoflorezjesusalirio@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-1214739567	Cédula de Ciudadanía	1214739567	YESICA		MARIA	TABARES	3128694814	YESI09072123@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-1216406	Cédula de Ciudadanía	1216406	ALEJANDRO		MONTAÑO		311 3489555	loriannys04vera@icloud.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1220471144	Cédula de Ciudadanía	1220471144	ANDREA		CORTES		305-619-9873	andreacotes87@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-123456789	Cédula de Ciudadanía	123456789	EMBAJADORA		CATALINA	JARAMILLO	SOLICITA TEL	ACTUALIZAR CORREO	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-13873460	Cédula de Ciudadanía	13873460	JULIAN		RIVERA		3175192397	Julianrivera.81@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-16209031	Cédula de Ciudadanía	16209031	MARIA		ALEJANDRA	RIVAS	17864124204	ferrer.gomez@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-20387333	Cédula de Ciudadanía	20387333	GINA		PAOLA	RODRIGUEZ	3042904747	Giraron18@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-20627238	Cédula de Ciudadanía	20627238	LEIDY		ANDREA	GONZALES	3115378452	andreagonzalezlopez@yahoo.es	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-21087900	Cédula de Ciudadanía	21087900	SANDRA		CRISTINA	RAMIREZ	3102928496	sandrita.ramirez@hotmail.com	24	3			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-21395278	Cédula de Ciudadanía	21395278	ROCIO		JARAMILLO		3146451720	ROCIOJARAMILLO26@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-21396882	Cédula de Ciudadanía	21396882	MARIA		VICTORIA	PARRA	3104431939	gerencia@syrseguros.com.co	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-21481522	Cédula de Ciudadanía	21481522	TERESITA		SOTO		3006155735	tedeni17@yahoo.com	17	10			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-21778111	Cédula de Ciudadanía	21778111	MARIA		EUGENIA	HOYOS	3012688598	maru3009@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-21831091	Cédula de Ciudadanía	21831091	MARGARITA		RAMIREZ		3223143649	mmrdh1946@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-22069021	Cédula de Ciudadanía	22069021	GLORIA		VALENCIA		3105255443	gloriaevalencia62@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-22081972	Cédula de Ciudadanía	22081972	FABIOLA		SALAZAR		3108219347	fabisa7@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-222222222	Cédula de Ciudadanía	222222222	CONSUMIDOR		FINAL		1234569869	FACTURACIONHEAVENCOMPANY@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-24228735	Cédula de Ciudadanía	24228735	MAYRA		ALEJANDRA	BETANCOURT	3003418948	mayra1975123@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-24731927	Cédula de Ciudadanía	24731927	CAROLINA		LOPEZ		3208067048	carolopezr@outlook.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-26441599	Cédula de Ciudadanía	26441599	MARICELA		RUBIO		3202352243	maruba2010@yahoo.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-28561762	Cédula de Ciudadanía	28561762	YASMIND		DIAZ	CASTRO	3123453239	YDCALPUJARRA10@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-29532422	Cédula de Ciudadanía	29532422	MARLENY		GOMEZ		3113579595	MAGOFI101@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-29567472	Cédula de Ciudadanía	29567472	BETTY		RIOS		3016244644	AAW_2128_3@icloud.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-30285726	Cédula de Ciudadanía	30285726	MARIA		GRISALES		3214925785	Negrilla_gris@hotmail.com	30	4			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-30402168	Cédula de Ciudadanía	30402168	LORENA		VILLEGAS		3104354889	LOREFV@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-30712419	Cédula de Ciudadanía	30712419	TERESA		GOMEZ		3108967737	teresadej58@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-311092	Cédula de Extranjería	311092	ALFONSO		MONGE		3007898328	ALFONSOMONGEU24@GMAIL.COM	6	8			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-31961068	Cédula de Ciudadanía	31961068	ESTER		CRESTY		3144420594	zlta55@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-32241000	Cédula de Ciudadanía	32241000	JOHANA		FERNANDEZ		3137678433	NANAFERNANDEZDURANGO@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-32242047	Cédula de Ciudadanía	32242047	LAUREN		PEÑA		3175011970	LAURENPE8@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-32242459	Cédula de Ciudadanía	32242459	PAMELA		FRANCO	MENESES	3001274690	PFM831@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-32257323	Cédula de Ciudadanía	32257323	LILIAN		JOHANA	OSPINA	3104158470	lilijosme@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-32258349	Cédula de Ciudadanía	32258349	CAROLINA		PELAEZ		3176580724	CARITOPEL@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-32295764	Cédula de Ciudadanía	32295764	JANETH		VILLA		3147140857	ajvc0327@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-32299041	Cédula de Ciudadanía	32299041	ANA		MARIA	ESPINOSA	3209639308	ANAMARIAESPINOSAO@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-32353013	Cédula de Ciudadanía	32353013	MARIA		ADELAIDA	GAVIRIA	3017659689	MARIAGAVIRIA945@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-32477222	Cédula de Ciudadanía	32477222	FABIOLA		PENAGOS		3007865952	ALEILARES@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-32543644	Cédula de Ciudadanía	32543644	NORA		PIEDRAHITA		3122580831	NEGRITAP126@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-32780120	Cédula de Ciudadanía	32780120	LILIANA		BARRETO		3114121757	lilianabarreto@intalent.com.co	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-32935726	Cédula de Ciudadanía	32935726	MEIRA		LUZ	PEREZ	3127202501	MEIDALUZ06@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-33994336	Cédula de Ciudadanía	33994336	MARCIA		MONTOYA		3234963172	TESORO@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-35198555	Cédula de Ciudadanía	35198555	ADRIANA		MILENA	ZAPATA	3125200209	adrif62@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-35459410	Cédula de Ciudadanía	35459410	GLORIA		ARANGO		3206987825	troquelsa1@une.net.co	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-35525646	Cédula de Ciudadanía	35525646	PILAR		SALCEDO		3175191879	pilarsalcedo03@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-355724	Cédula de Extranjería	355724	ZSUSANNA		MALOMHEGYI		3137754594	Zsuzsamalo@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-36298472	Cédula de Ciudadanía	36298472	ERIKA		WIEDERKEHR		36298472	Erikauga24@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-36754661	Cédula de Ciudadanía	36754661	YULI		GOMEZ		3104472882	yulyxgomez@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-37444430	Cédula de Ciudadanía	37444430	LILIANA		URIBE		3117111680	LILIANA.URIBE31@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-37841567	Cédula de Ciudadanía	37841567	ANDREA		KATHERINE	VIDAL	3175192397	andreakvidal12@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-38142469	Cédula de Ciudadanía	38142469	AURA		CAROLINA	CRUZ	3108618179	auraccruz@yahoo.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-38262991	Cédula de Ciudadanía	38262991	ISABEL		JAUREGUI		3152996955	isajaureguivallejo@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-38942917	Cédula de Ciudadanía	38942917	MARTHA		CECILIA	MOSSOS	3133942279	marthamossos@yahoo.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-39176764	Cédula de Ciudadanía	39176764	LILIANA		LOPEZ	VALENCIA	3174010077	Llopezva@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-39281547	Cédula de Ciudadanía	39281547	YERICA		JARAMILLO		3147342563	YEJARA16@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-39412621	Cédula de Ciudadanía	39412621	CLAUDIA		ELENA	URANGO	3137571910	CLAUDIA1002.ELENA@GMAIL.COM	1	8			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-39695567	Cédula de Ciudadanía	39695567	MONICA		ROJAS		30020856812	MROJAS0466@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-39721468	Cédula de Ciudadanía	39721468	MONICA		BOJACA		3134916030	ana.gb@outlook.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-39791787	Cédula de Ciudadanía	39791787	TATIANA		SANTA	CRUZ	3124546056	SANTACRUZ.TATIANA@HOTMAIL.COM	6	5			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-40411225	Cédula de Ciudadanía	40411225	MONICA		LAYTON		3108070683	molayton@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-41892976	Cédula de Ciudadanía	41892976	MARTHA		GIRALDO		15167276327	MARTHAG976@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-41952188	Cédula de Ciudadanía	41952188	LUZ		JIMENEZ		3102483588	Nata.x7@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-42030194	Cédula de Ciudadanía	42030194	ADRIANA		FELISA	PEREZ	3108711837	felisaperez218@gmail.com	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-42057470	Cédula de Ciudadanía	42057470	RUBIELA		ZULETA		3116216116	tesorocatalinajaramillo@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-42105755	Cédula de Ciudadanía	42105755	PATRICIA		SANDOVAL	VERGARA	3103473083	patricia.sandoval181@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-42688945	Cédula de Ciudadanía	42688945	STELLA		ANTOLINEZ	CADAVID	3135615601	Antolinez27@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-42761330	Cédula de Ciudadanía	42761330	MARIA		EUGENIA	QUIROZ	3104213643	mquiroz@confianza.com.co	\N	\N			sede-cj-medical-el-tesoro			t	2026-09-20 00:52:54.234108	
cli-42766441	Cédula de Ciudadanía	42766441	JOSEFINA		PEREZ		3225016397	CONSULTORIOMARIOFRANCO@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-42779460	Cédula de Ciudadanía	42779460	LUCELLY		PENAGOS		3116056317	lupeva80@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-42789487	Cédula de Ciudadanía	42789487	DUVER		CAVADID	ACEVEDO	3206288789	DAYACADAVID@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-42799736	Cédula de Ciudadanía	42799736	DIANA		ALEJANDRA	FERNANDEZ	3147741816	Jardindetendencias@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-42824198	Cédula de Ciudadanía	42824198	LINA		LONDOÑO		3113728161	LINALONDONOC@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-42827722	Cédula de Ciudadanía	42827722	SARA		ALVAREZ		3046300660	Aqsara470@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-42828462	Cédula de Ciudadanía	42828462	KATHERINE		ÁLVAREZ	RESTREPO	3103813400	kathya_51@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-42868110	Cédula de Ciudadanía	42868110	SUSANA		VELEZ		3108419623	SUSANAVELEZG@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-42872645	Cédula de Ciudadanía	42872645	GLORIA	CECILIA	CORREA	GALEANO	3155301688	GLORIA.CORREA@PRO-PONEMOS.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-42880332	Cédula de Ciudadanía	42880332	ANA		VILLEGAS		3165269927	alvillegas19@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-42883048	Cédula de Ciudadanía	42883048	NORA		ELENA	CARDONA	312 2573180	CARDONANORA19@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-42888483	Cédula de Ciudadanía	42888483	ADRIANA		ESPINOSA		3103749801	ADRIANAMESPINOSA@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-42898873	Cédula de Ciudadanía	42898873	CLARA		CORREA		3015493909	CLAICOVA@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-42964420	Cédula de Ciudadanía	42964420	BEATRIZ		GARCÍA		3108966504	jaramillogarcia22@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-42979373	Cédula de Ciudadanía	42979373	MARTHA		BOTERO		3117693734	boteromarta72@gamil.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-42982544	Cédula de Ciudadanía	42982544	CRISTINA		DAPENA		3104265162	CRISDAPENA@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43017003	Cédula de Ciudadanía	43017003	MATHA		ARIAS		3216142010	Maluariasm@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-43017004	Cédula de Ciudadanía	43017004	MARTHA		ARIAS		3216142010	Maluariasm@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43035312	Cédula de Ciudadanía	43035312	PAULINA		VALENCIA		3113973518	PAULINAFK2011@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43080476	Cédula de Ciudadanía	43080476	ILVA		STELLA	OSORIO	3103892775	stellaoza@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43089021	Cédula de Ciudadanía	43089021	LUZ		MARINA	MONTOYA	3104532165	luzma.6563@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43089123	Cédula de Ciudadanía	43089123	MARTHA		GAVIRIA		3155018553	MARTHAGAVIRIAMENDEZ@GMAIL.COM	1	8			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43109347	Cédula de Ciudadanía	43109347	ALEJANDRA		MARIA	RUIZ	3128962409	MIPULGAAMRUIZ@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43110114	Cédula de Ciudadanía	43110114	DIANA		VARGAS	AGUIRRE	3182186324	DIANAVARGAS79@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43110374	Cédula de Ciudadanía	43110374	EVELIN		RONCALLO		3188832453	evelynroncallo@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43115783	Cédula de Ciudadanía	43115783	MARGOTH		TORRO		3176791146	margorttorre3812@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-43117859	Cédula de Ciudadanía	43117859	MONICA		GUERRA		3127837104	tesoro@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43167251	Cédula de Ciudadanía	43167251	CLARA		ANDREA	BRIÑER	3205510005	ANDREBMAXIMO5@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43205728	Cédula de Ciudadanía	43205728	ISABEL		CRISTINA	VELASQUEZ	3122751219	isabelcristina8012@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43220638	Cédula de Ciudadanía	43220638	NATALIA		MEJIA	BETANCUR	3137183440	nmejia1114@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43251799	Cédula de Ciudadanía	43251799	ANDREA		BETANCUR		3157811738	DREUSS81@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43253935	Cédula de Ciudadanía	43253935	LIGIA		ELENA	DAVID	3187462559	elenadavidgraciano2016@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43256482	Cédula de Ciudadanía	43256482	ANA		MARIA	VELASQUEZ	3206958394	ANAMAVELAS11@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43258723	Cédula de Ciudadanía	43258723	ELIZA		CARRASCAL		3183123920	ELICARRASCALM@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43260411	Cédula de Ciudadanía	43260411	CATALINA		MONTOYA		3012096029	catamon28@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43272513	Cédula de Ciudadanía	43272513	ANGELA	CRISTINA	LOMBANA	ARIAS	3103662001	angelalombana81@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43400673	Cédula de Ciudadanía	43400673	CATALINA		HERNANDEZ		3186742516	CATALINAHERNANDEZ23@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43491005	Cédula de Ciudadanía	43491005	LUZ		ADRIANA	SUAREZ	3137192836	LASUAREZA2009@GMAIL.COM	27	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43506547	Cédula de Ciudadanía	43506547	ETNA		RUTH	ZULETA	3004690166	EMESAZ@YAHOO.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43525709	Cédula de Ciudadanía	43525709	MARISOL		MEDINA		3053446020	solmedina3@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43532117	Cédula de Ciudadanía	43532117	CLAUDIA	PATRICIA	MAYA	RAMIREZ	3103735423	CLAUDIAP.MAYA@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-43533913	Cédula de Ciudadanía	43533913	DIANA	ISABEL	RESTREPO	HENAO	3206995874	disarpo@yafu.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43535108	Cédula de Ciudadanía	43535108	MARIA		DORIBEL	TORRES	3172200062	Dtorres913@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43538681	Cédula de Ciudadanía	43538681	MONICA		RODRIGUEZ		3122951234	MONICA@CLICHECOLOMBIA.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43556681	Cédula de Ciudadanía	43556681	ASTRID		HOLGUIN		3174033705	AHOLGIN0311@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43567026	Cédula de Ciudadanía	43567026	NELLY		ARIAS		3195135306	NELLYAMPAROARIAS@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43571311	Cédula de Ciudadanía	43571311	ELIZABETH		JIMENEZ		3127894910	SBPERFILFRANCEZ@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43594009	Cédula de Ciudadanía	43594009	Dalia		Andrea	Giraldo	3116597525	dalia2giraldo@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43602238	Cédula de Ciudadanía	43602238	LUZ		QUIROZ		3122629007	luzaje@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43614016	Cédula de Ciudadanía	43614016	CLAUDIA		SANTAMARIA		3015577523	info@masscreaccion.com	\N	\N			sede-cj-medical-el-tesoro			t	2026-09-20 00:52:54.234108	
cli-43616101	Cédula de Ciudadanía	43616101	PASCUALINA		CRISPINO		3008944008	pcrispinom@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43619949	Cédula de Ciudadanía	43619949	SANDRA		ALZATE		3164736247	sialzateb@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43623570	Cédula de Ciudadanía	43623570	ANDREA		PEREZ		3103500370	ANDRE.PEREZ2376@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43627259	Cédula de Ciudadanía	43627259	MARIA		LUISA	BOTERO	3052475745	LULUPALUSA@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43628557	Cédula de Ciudadanía	43628557	ALEXANDRA		HERRERA	QUIJANO	3127716404	alexhq557@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43640875	Cédula de Ciudadanía	43640875	MILENA		ISABEL	RUIZ	3103822802	RUIZARA026@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43653810	Cédula de Ciudadanía	43653810	SANDRA		RESTREPO	BARRIENTO	3012798819	SAEREBA@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-43725432	Cédula de Ciudadanía	43725432	ANA	JULIA	SOTO	MONTOYA	3108226144	Anajuliasotmont@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43743970	Cédula de Ciudadanía	43743970	MARIANA		MUÑOZ	LOPEZ	3217188813	marianamunoz74@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43746775	Cédula de Ciudadanía	43746775	GIRLESA		HERNANDEZ		3016704393	hernandezgirlesa3@gmail.com	11	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43750606	Cédula de Ciudadanía	43750606	Yohaira		Gomez		3187356427	yohairag43@gmail.com	8	1			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43757644	Cédula de Ciudadanía	43757644	ANGELICA	MARIA	OSORIO	PELAEZ	3116104800	AMOSORIOP@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43757888	Cédula de Ciudadanía	43757888	MARIA		CRISTINA	ISAZA	3127945485	mcisaza7@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43840585	Cédula de Ciudadanía	43840585	DIANA		MILENA	CORREA	3007972087	Pereacorreasofia@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-43867018	Cédula de Ciudadanía	43867018	LINA	MARIA	JARAMILLO	ECHEVERRI	3164782770	linajaramillo@seti.com.co	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43868433	Cédula de Ciudadanía	43868433	MARCELA		PÉREZ		3116340935	MARCELAPEREZC@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43869520	Cédula de Ciudadanía	43869520	Soraya		Gómez		3125844479	sorayaballesteros4@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43869810	Cédula de Ciudadanía	43869810	MARITZA		RIVILLAS		3242503336	maritzarivi@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43870466	Cédula de Ciudadanía	43870466	CAMILA		VELEZ		3174389997	camivelez@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43874449	Cédula de Ciudadanía	43874449	LINA		MARIA	CARDONA	3128505742	GERENCIA@ALUMCOR.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43877210	Cédula de Ciudadanía	43877210	JOHANA		URIBE	VELEZ	3223444726	JANAURIBE@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43878034	Cédula de Ciudadanía	43878034	ANA		ISABEL	RIVERA	3148320926	airoftalmologa@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-43907401	Cédula de Ciudadanía	43907401	KAROL		TABIMA		3148112506	Karey8210@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43971658	Cédula de Ciudadanía	43971658	Natalia		Miravay		3007835868	nmparango27@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43973519	Cédula de Ciudadanía	43973519	DIANA		OSPINA		322 5884142	GUADALUPE.OSPINA1025@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43976430	Cédula de Ciudadanía	43976430	ALEJANDRA		MEDINA		3042215110	ALMEGO113@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-43979089	Cédula de Ciudadanía	43979089	CATALINA		MARIN	MEDINA	3108422497	catalina_marin.medina@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43979215	Cédula de Ciudadanía	43979215	LUISA		MOLINA		3146619813	CRESPOCRISPI@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-43986250	Cédula de Ciudadanía	43986250	PAULA		ANDREA	URREGO	3108482075	PAONML.A@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-444444296	Cédula de Ciudadanía	444444296	lUZ		DALYS	DIOSA	17187372302	ANDRES.TOBON.F@GMAIL.COM	10	12			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-444444336	Cédula de Ciudadanía	444444336	BENJAMIN		GARNICA		50766239904	bgarnica@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-444444388	Cédula de Ciudadanía	444444388	MARIA		TERESA	ARENAS	3004843946	MARIATERESARENAS10@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-49723010	Cédula de Ciudadanía	49723010	LILIBETH		MENESES	DAZA	3003213398	lilimenesesd@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-50922034	Cédula de Ciudadanía	50922034	MARIA		ROSA	MARTINEZ	3227937286	mcmariar6803@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-51561728	Cédula de Ciudadanía	51561728	Flor		Angela	Zapata	3195731396	florangela3@yahoo.com.es	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-51874849	Cédula de Ciudadanía	51874849	CLAUDIA	SOLER	MARIA	PARRA	3138878201	csolarespa@osteganos.net	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-51935765	Cédula de Ciudadanía	51935765	ROCIO		QUIROZ		3123440654	luzrocioquiros@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-51951488	Cédula de Ciudadanía	51951488	MARTHA		GUZMAN		3017139419	MARTHAGUZRI@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-51976440	Cédula de Ciudadanía	51976440	ANGELA		PATRICIA	GARCIA	3174287858	APGARZA1@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-52015593	Cédula de Ciudadanía	52015593	YANETH		MENDOZA		3115035680	YANETHMEN13@HOTMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52024703	Cédula de Ciudadanía	52024703	SOFIA		TOLEDO		3133955735	cayatoledo@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52069804	Cédula de Ciudadanía	52069804	NANCY		ESPERANZA	CARDONA	3233921792	Nancy.1108c@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52108151	Cédula de Ciudadanía	52108151	JULIA		MERCEDES	CASTELLANOS	3142661917	kancan@hotmail.co.uk	28	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52151950	Cédula de Ciudadanía	52151950	XIMENA		CASARES		3012869571	XIMENA72@YAHOO.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52252979	Cédula de Ciudadanía	52252979	KAROLINA		PINZON		3143024554	caroteo@yahoo.es	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52273577	Cédula de Ciudadanía	52273577	Maria		Jose	Silva	3054646670	Silva01janeth@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52295932	Cédula de Ciudadanía	52295932	ANGELA		MARTINEZ		3214900672	AELIANAMARTINEZ@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52298527	Cédula de Ciudadanía	52298527	LILIANA	PATRICIA	HERNANDEZ	BOLIVAR	3044783514	FHERRERA.SEGUROS@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52329181	Cédula de Ciudadanía	52329181	LUZ		MARIA	RAMIREZ	3152658813	Luzmariaramirezmahecha@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52417541	Cédula de Ciudadanía	52417541	ANA		MILENA	FIERRO	3007079252	ANA1_FIERRO@HOTMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52426985	Cédula de Ciudadanía	52426985	ALEXANDRA		PAEZ		3133839133	paezalexandra@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52429996	Cédula de Ciudadanía	52429996	YAZMIN		MONROY		3148797994	Monroyyazmin683@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52441707	Cédula de Ciudadanía	52441707	ANGELA		MILENA	ARIZA	3115567575	angelaariza@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52496376	Cédula de Ciudadanía	52496376	MARCELA		VIZCAINO		3208858368	Jmarcelavj06@hotmail.com	6	4			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52520940	Cédula de Ciudadanía	52520940	YEINY		SÁNCHEZ	CARDENAS	3017151335	YEINYSANCHEZ@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-52521159	Cédula de Ciudadanía	52521159	YINA		PAOLA	ÑAÑEZ	3113149157	yinananezortiz@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52536110	Cédula de Ciudadanía	52536110	CARMEN		PARDA		3027244523	LUPEPRADA79@HOTMAIL.COM	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-52546874	Cédula de Ciudadanía	52546874	ANA		LEAL		3214293329	ana.ana.mxd@gmail.com	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-52562642	Cédula de Ciudadanía	52562642	SANDRA		PUENTES		3133919509	sppr26@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52694094	Cédula de Ciudadanía	52694094	ANGELA		ROJAS		3108161777	angierojas1607@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52712795	Cédula de Ciudadanía	52712795	LILIANA		PINEDA		3202334427	lilianapril.fr@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52791664	Cédula de Ciudadanía	52791664	MARCELA		DELGADO		3213222525	gmarcela.delgado@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52937855	Cédula de Ciudadanía	52937855	LUZ		ANGELA	ANGULO	3143410731	ANGELITO.ANGEL@HOTMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52961768	Cédula de Ciudadanía	52961768	JULY		CAROLINA	MIRANDA	3004078890	julycarolina.miranda@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52965240	Cédula de Ciudadanía	52965240	DIANA		PAOLA	MONTAÑO	3057620093	diamonram@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52974508	Cédula de Ciudadanía	52974508	MARCELA		TALERO		3125577488	MARCEBAS@HOTMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-52983883	Cédula de Ciudadanía	52983883	JEIMY		PAOLA	RAMOS	3209011220	ramos312015@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-52989297	Cédula de Ciudadanía	52989297	ANGELICA		MARIA	CARDONA	3104164370	ccpicnic@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-53001656	Cédula de Ciudadanía	53001656	LINA		ROSY		3185163393	rossilina@gmail.com	4	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-53011725	Cédula de Ciudadanía	53011725	INGRID		BELLO		3002002385	ingridlilianabello@gmail.com	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-53013834	Cédula de Ciudadanía	53013834	Ana		Maria	Carrillo	3174300307	anama119@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-53015367	Cédula de Ciudadanía	53015367	DIANA		CAROLINA	IBAÑEZ	3177992349	DIANACAROLINA.IBANEZ@OUTLOOK.COM	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-53051254	Cédula de Ciudadanía	53051254	ERIKA		JASMIN	FIGUEROA	3156711721	tesoro@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-53067438	Cédula de Ciudadanía	53067438	ESTEFANNY		BELTRAN	GALEANO	3124786040	Stefanny.beltrang@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-53074208	Cédula de Ciudadanía	53074208	LADY		MARIANA	RODRIGUEZ	3144222139	LADYJOSHER@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-53106872	Cédula de Ciudadanía	53106872	NATALIA		RODRIGUEZ		3188273590	NATHARO935@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-53177401	Cédula de Ciudadanía	53177401	JULIANA		QUINTERO		3206337293	juli_quintero@hotmail.com	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-55305950	Cédula de Ciudadanía	55305950	VANESA		REMOM		3022462684	VANEREMOM0707@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-599953	Cédula de Ciudadanía	599953	MAIRETH		PALACIOS		3046190191	briger@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-63316600	Cédula de Ciudadanía	63316600	LEICY		PARRA		3155951522	LEICY@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-63335205	Cédula de Ciudadanía	63335205	RUBBY		DURAN		3214492351	rubbyduranm@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-63499559	Cédula de Ciudadanía	63499559	CLAUDIA		BOHORQUEZ		3118033579	cbohorquezobregon@gmail.com	\N	\N			sede-cj-medical-bogota	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-63523969	Cédula de Ciudadanía	63523969	CARMEN		MONSALVE		3205193771	carmenromonsalve@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-64584341	Cédula de Ciudadanía	64584341	KAREN		GOMEZ		3015960052	KARENPATRYG19@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-66738837	Cédula de Ciudadanía	66738837	MARISOL		CALLE		3003221646	MARISOL_CALLE@HOTMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-79896515	Cédula de Ciudadanía	79896515	FRANCISCO		SANCHEZ		3193913024	FRANCISCOZARATE78Q@GMAIL.COM	\N	\N			sede-cj-medical-bogota	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-8089948	Cédula de Ciudadanía	8089948	SAHAND		JALALI		3028069842	sahandjalali@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-8106080	Cédula de Ciudadanía	8106080	JULIAN		RIOS		3007111263	JRIOSESC@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 00:52:54.234108	
cli-8163328	Cédula de Ciudadanía	8163328	SANTIAGO		ALVAREZ		3104743065	santiagoalvarez198304@gmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-974407	Cédula de Extranjería	974407	ANABEL		GUERRERO		50767812042	AMGH1991@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Primer Vez		t	2026-09-20 00:52:54.234108	
cli-98562114	Cédula de Ciudadanía	98562114	DIEGO		MARTINEZ	QUINTERO	3014493366	DIGO.MARI10@GMAIL.COM	\N	\N			sede-cj-medical-el-tesoro	Cliente Recurrente		t	2026-09-20 00:52:54.234108	
cli-1000084923	Cédula de Ciudadanía	1000084923	ANLLI		VANESSA	RUIZ	3232045895	anllivanesaruiz23@hotmail.com	\N	\N			sede-cj-medical-el-tesoro	Cliente Leal		t	2026-09-20 19:23:29.694908	
\.


--
-- Data for Name: citas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.citas (id, tipo, fecha, inicio, fin, especialista_id, sede_id, servicio_id, cliente_id, estado_id, canal, asignada_por, notas, motivo, reprogramada_de, reprogramada_a, importado, creado_en, creado_por, ocupa_cupo) FROM stdin;
imp-1	cita	2026-06-01	09:00:00	09:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1000707166	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-09 00:00:00		t
imp-10	cita	2026-06-03	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51874849	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-05-27 00:00:00		t
imp-100	cita	2026-06-04	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43260411	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-1000	cita	2026-08-13	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-32780120	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		t
imp-1001	cita	2026-08-13	12:00:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-xs	cli-1042771641	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-05 00:00:00		f
imp-1002	cita	2026-08-13	12:00:00	12:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-32780120	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-13 00:00:00		f
imp-1003	cita	2026-08-13	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1032406074	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-13 00:00:00		t
imp-1004	cita	2026-08-13	13:30:00	14:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1121825659	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-12 00:00:00		f
imp-1005	cita	2026-08-13	14:00:00	14:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-32780120	est-cumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-13 00:00:00		t
imp-1006	cita	2026-08-13	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1121825659	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-12 00:00:00		f
imp-1007	cita	2026-08-13	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-32780120	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-13 00:00:00		t
imp-1008	cita	2026-08-13	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1018456833	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-10 00:00:00		t
imp-1009	cita	2026-08-13	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1019029968	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		t
imp-101	cita	2026-06-05	09:00:00	09:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-32477222	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-1010	cita	2026-08-14	09:00:00	09:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020798300	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1011	cita	2026-08-14	09:00:00	09:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020798300	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-1012	cita	2026-08-14	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020715074	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-29 00:00:00		f
imp-1013	cita	2026-08-14	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020715074	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-13 00:00:00		t
imp-1014	cita	2026-08-14	10:00:00	10:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1144134987	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-04 00:00:00		t
imp-1015	cita	2026-08-14	10:30:00	11:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020715074	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-10 00:00:00		f
imp-1016	cita	2026-08-14	10:30:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-xs	cli-1001854605	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-06 00:00:00		f
imp-1017	cita	2026-08-14	10:30:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-xs	cli-1001854605	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-06 00:00:00		f
imp-1018	cita	2026-08-14	11:30:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-xs	cli-1001854605	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-08 00:00:00		t
imp-1019	cita	2026-08-14	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1020758898	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-12 00:00:00		t
imp-102	cita	2026-06-05	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1125795486	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-05-25 00:00:00		f
imp-1020	cita	2026-08-14	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1102840319	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1021	cita	2026-08-14	15:00:00	15:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1022	cita	2026-08-14	15:30:00	16:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1023	cita	2026-08-14	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1143337034	est-incumplido	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-08-13 00:00:00		t
imp-1024	cita	2026-08-14	16:00:00	16:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1018456833	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		f
imp-1025	cita	2026-08-14	16:30:00	17:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1141520024	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1026	cita	2026-08-14	16:30:00	17:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1141520024	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-1027	cita	2026-08-14	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1121825659	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-13 00:00:00		t
imp-1028	cita	2026-08-14	18:00:00	18:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1121825659	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-13 00:00:00		t
imp-1029	cita	2026-08-15	09:00:00	09:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1024543929	est-cancelado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		f
imp-103	cita	2026-06-05	11:00:00	11:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1037648065	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-1030	cita	2026-08-15	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1014305681	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-03 00:00:00		t
imp-1031	cita	2026-08-15	10:00:00	10:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1107069165	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1032	cita	2026-08-15	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1022341860	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1033	cita	2026-08-15	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1121825659	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		f
imp-1034	cita	2026-08-15	12:30:00	13:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1121825659	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		f
imp-1035	cita	2026-08-15	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-carbon-peel	cli-1037644195	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-08 00:00:00		t
imp-1036	cita	2026-08-15	15:00:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-xs	cli-1037644195	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-08 00:00:00		t
imp-1037	cita	2026-08-20	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1026254692	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-08-18 00:00:00		f
imp-1038	cita	2026-08-20	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1026254692	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-14 00:00:00		f
imp-1039	cita	2026-08-20	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-52329181	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		f
imp-104	cita	2026-06-05	11:00:00	11:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1037648065	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-1040	cita	2026-08-20	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-52329181	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1041	cita	2026-08-20	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-52069804	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		f
imp-1042	cita	2026-08-20	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1015452061	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		t
imp-1043	cita	2026-08-20	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-52069804	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		f
imp-1044	cita	2026-08-20	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-52069804	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		t
imp-1045	cita	2026-08-20	12:00:00	12:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-53074208	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		f
imp-1046	cita	2026-08-20	12:00:00	12:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1015452989	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		f
imp-1047	cita	2026-08-20	12:00:00	12:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1015452989	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1048	cita	2026-08-20	12:30:00	12:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52961768	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		f
imp-1049	cita	2026-08-20	14:00:00	14:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-53074208	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		t
imp-105	cita	2026-06-05	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1000655431	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-1050	cita	2026-08-20	14:30:00	15:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1026266784	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-12 00:00:00		t
imp-1051	cita	2026-08-20	15:00:00	15:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1024540490	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-12 00:00:00		f
imp-1052	cita	2026-08-20	15:30:00	16:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-42030194	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-12 00:00:00		f
imp-1053	cita	2026-08-20	15:30:00	16:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-42030194	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1054	cita	2026-08-20	16:00:00	16:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-51935765	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-1055	cita	2026-08-20	16:30:00	16:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52961768	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1056	cita	2026-08-20	16:30:00	16:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52961768	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		f
imp-1057	cita	2026-08-20	17:00:00	17:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-20627238	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-20 00:00:00		t
imp-1058	cita	2026-08-20	17:00:00	17:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-consulta-medica	cli-52521159	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		f
imp-1059	cita	2026-08-20	17:00:00	17:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52521159	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		f
imp-106	cita	2026-06-05	15:00:00	15:20:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1036607047	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-1060	cita	2026-08-20	17:30:00	18:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1032423777	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		t
imp-1061	cita	2026-08-20	18:00:00	18:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-52015593	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1062	cita	2026-08-21	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1026254692	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		f
imp-1063	cita	2026-08-01	09:00:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-43117859	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1064	cita	2026-08-01	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-carbon-peel	cli-43117859	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1065	cita	2026-08-01	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32257323	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-1066	cita	2026-08-01	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-24 00:00:00		f
imp-1067	cita	2026-08-01	16:00:00	16:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1001140449	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-23 00:00:00		f
imp-1068	cita	2026-08-01	16:00:00	16:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1001140449	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-31 00:00:00		f
imp-1069	cita	2026-08-01	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037622259	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-107	cita	2026-06-05	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42789487	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-1070	cita	2026-08-03	10:00:00	10:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1007353470	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-1071	cita	2026-08-03	10:00:00	10:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-32935726	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-01 00:00:00		t
imp-1072	cita	2026-08-03	10:30:00	11:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-42979373	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-1073	cita	2026-08-03	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152193761	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-29 00:00:00		f
imp-1074	cita	2026-08-03	11:30:00	12:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-radiofrecuencia-fraccionada-alta-intensidad	cli-123456789	est-confirmado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-31 00:00:00		t
imp-1075	cita	2026-08-03	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152193761	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-03 00:00:00		t
imp-1076	cita	2026-08-03	16:00:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1128438388	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-03 00:00:00		t
imp-1077	cita	2026-08-03	16:30:00	16:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1034991123	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-1078	cita	2026-08-03	17:00:00	17:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-52562642	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-03 00:00:00		t
imp-1079	cita	2026-08-03	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-63316600	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-29 00:00:00		f
imp-108	cita	2026-06-05	15:30:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-42789487	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-1080	cita	2026-08-04	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43251799	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-1081	cita	2026-08-04	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1053789864	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-28 00:00:00		f
imp-1082	cita	2026-08-04	10:30:00	10:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-43251799	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-1083	cita	2026-08-04	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1036614057	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-03 00:00:00		t
imp-1084	cita	2026-08-04	11:30:00	12:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-1004999021	est-cumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-03 00:00:00		t
imp-1085	cita	2026-08-04	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1107072156	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-04 00:00:00		t
imp-1086	cita	2026-08-05	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1130667990	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-01 00:00:00		t
imp-1087	cita	2026-08-05	10:00:00	10:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-38142469	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-24 00:00:00		t
imp-1088	cita	2026-08-05	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1041151982	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-31 00:00:00		f
imp-1089	cita	2026-08-05	10:30:00	10:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-43757888	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-109	cita	2026-06-05	16:00:00	16:20:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1034993103	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-02 00:00:00		t
imp-1090	cita	2026-08-05	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1041151982	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-31 00:00:00		f
imp-1091	cita	2026-08-05	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43757888	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-05 00:00:00		t
imp-1092	cita	2026-08-05	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1041151982	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-05 00:00:00		t
imp-1093	cita	2026-08-05	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1041151982	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-05 00:00:00		t
imp-1094	cita	2026-08-05	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017126454	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1095	cita	2026-08-05	14:30:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43571311	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1096	cita	2026-08-05	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43571311	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1097	cita	2026-08-05	16:30:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1088304912	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-05 00:00:00		t
imp-1098	cita	2026-08-06	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43602238	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-1099	cita	2026-08-06	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-28561762	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-04 00:00:00		t
imp-11	cita	2026-06-03	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51874849	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-05-27 00:00:00		f
imp-110	cita	2026-06-05	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1094977327	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-1100	cita	2026-08-06	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1015478534	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		f
imp-1101	cita	2026-08-06	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42880332	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-04 00:00:00		t
imp-1102	cita	2026-08-06	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42880332	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-05 00:00:00		t
imp-1103	cita	2026-08-06	13:00:00	13:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1037591863	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-03 00:00:00		t
imp-1104	cita	2026-08-06	13:00:00	13:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1037591863	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-03 00:00:00		f
imp-1105	cita	2026-08-06	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-42872645	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-06 00:00:00		f
imp-1106	cita	2026-08-06	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-43979215	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1107	cita	2026-08-06	15:00:00	15:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1037608047	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1108	cita	2026-08-06	15:00:00	15:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1036607047	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1109	cita	2026-08-06	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-38942917	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-111	cita	2026-06-05	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42789487	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-1110	cita	2026-08-06	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-13873460	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		t
imp-1111	cita	2026-08-06	16:30:00	17:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43971658	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-31 00:00:00		f
imp-1112	cita	2026-08-06	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42789487	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1113	cita	2026-08-06	17:00:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1040515348	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1114	cita	2026-08-06	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-37841567	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		t
imp-1115	cita	2026-08-08	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-22081972	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1116	cita	2026-08-08	11:00:00	11:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43757888	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-05 00:00:00		t
imp-1117	cita	2026-08-08	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036620763	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-08 00:00:00		t
imp-1118	cita	2026-08-08	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036620763	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-1119	cita	2026-08-08	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-8163328	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-112	cita	2026-06-05	17:00:00	17:20:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1125598288	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-1120	cita	2026-08-08	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-8163328	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-08 00:00:00		t
imp-1121	cita	2026-08-08	15:00:00	16:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-1125598715	est-confirmado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-03 00:00:00		t
imp-1122	cita	2026-08-08	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-52298527	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-1123	cita	2026-08-08	16:30:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1037571876	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-08 00:00:00		t
imp-1124	cita	2026-08-10	09:00:00	09:45:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-toxina-botox	cli-1090547471	est-confirmado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-08 00:00:00		t
imp-1125	cita	2026-08-10	09:00:00	09:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1090547471	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-10 00:00:00		f
imp-1126	cita	2026-08-10	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-1125598288	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-08 00:00:00		f
imp-1127	cita	2026-08-10	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-1152442530	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-08 00:00:00		f
imp-1128	cita	2026-08-10	09:30:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1152442530	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-10 00:00:00		t
imp-1129	cita	2026-08-10	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1036631947	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-05 00:00:00		f
imp-113	cita	2026-06-05	17:30:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1152192832	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-1130	cita	2026-08-10	10:00:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1152442530	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-10 00:00:00		t
imp-1131	cita	2026-08-10	10:00:00	10:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1007353470	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-03 00:00:00		t
imp-1132	cita	2026-08-10	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-1152442530	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-10 00:00:00		t
imp-1133	cita	2026-08-10	11:00:00	11:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43556681	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-23 00:00:00		t
imp-1134	cita	2026-08-10	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-123456789	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-08-08 00:00:00		t
imp-1135	cita	2026-08-10	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-123456789	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-28 00:00:00		f
imp-1136	cita	2026-08-10	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-12022353	est-pendiente	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1137	cita	2026-08-10	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-1128271921	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-08 00:00:00		t
imp-1138	cita	2026-08-10	11:30:00	11:50:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-43907401	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-03 00:00:00		t
imp-1139	cita	2026-08-10	14:00:00	14:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1125598288	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-10 00:00:00		t
imp-114	cita	2026-06-05	17:30:00	17:50:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1125598288	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-1140	cita	2026-08-10	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-52298527	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1141	cita	2026-08-10	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-1063144451	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-10 00:00:00		t
imp-1142	cita	2026-08-11	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43110114	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1143	cita	2026-08-11	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-12022353	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		t
imp-1144	cita	2026-08-11	14:00:00	14:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1046666281	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-11 00:00:00		t
imp-1145	cita	2026-08-11	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1032418627	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		t
imp-1146	cita	2026-08-11	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43870466	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-07 00:00:00		t
imp-1147	cita	2026-08-12	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42824198	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-22 00:00:00		t
imp-1148	cita	2026-08-12	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1013612199	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1149	cita	2026-08-12	10:00:00	10:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1013612199	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-115	cita	2026-06-06	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-8106080	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-1150	cita	2026-08-12	10:30:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-radiofrecuencia-fraccionada-alta-intensidad	cli-98562114	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-12 00:00:00		f
imp-1151	cita	2026-08-12	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-42824198	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-12 00:00:00		t
imp-1152	cita	2026-08-12	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-444444296	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-12 00:00:00		t
imp-1153	cita	2026-08-12	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-444444296	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-12 00:00:00		t
imp-1154	cita	2026-08-12	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-98562114	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-12 00:00:00		t
imp-1155	cita	2026-08-12	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1115087263	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-22 00:00:00		t
imp-1156	cita	2026-08-12	14:30:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43571311	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-04 00:00:00		t
imp-1157	cita	2026-08-12	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43571311	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-04 00:00:00		f
imp-1158	cita	2026-08-13	13:00:00	13:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1036631947	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-10 00:00:00		t
imp-1159	cita	2026-08-13	13:30:00	14:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1128273353	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-10 00:00:00		f
imp-116	cita	2026-06-06	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43535108	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-16 00:00:00		t
imp-1160	cita	2026-08-13	15:30:00	15:50:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-36298472	est-confirmado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-13 00:00:00		t
imp-1161	cita	2026-08-13	16:00:00	16:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1128273353	est-cancelado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-08-11 00:00:00		f
imp-1162	cita	2026-08-13	16:00:00	16:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1128273353	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-13 00:00:00		t
imp-1163	cita	2026-08-14	09:00:00	09:30:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-43627259	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-1164	cita	2026-08-14	09:30:00	10:00:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-39176764	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-1165	cita	2026-08-14	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43538681	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-21 00:00:00		f
imp-1166	cita	2026-08-14	09:30:00	10:15:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43538681	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		t
imp-1167	cita	2026-08-14	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43628557	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1168	cita	2026-08-14	10:00:00	10:45:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43628557	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		f
imp-1169	cita	2026-08-14	10:00:00	10:30:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1036627141	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-117	cita	2026-06-06	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-42779460	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-30 00:00:00		f
imp-1170	cita	2026-08-14	10:00:00	10:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1020404375	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-1171	cita	2026-08-14	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1090493435	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-27 00:00:00		f
imp-1172	cita	2026-08-14	10:30:00	11:15:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1090493435	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		t
imp-1173	cita	2026-08-14	11:00:00	11:20:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1042771641	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-12 00:00:00		t
imp-1174	cita	2026-08-14	11:30:00	12:00:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1042771641	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		f
imp-1175	cita	2026-08-14	11:30:00	12:00:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1128397229	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-1176	cita	2026-08-14	12:00:00	12:30:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-32241000	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-1177	cita	2026-08-14	12:30:00	13:00:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1152188224	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-1178	cita	2026-08-14	13:30:00	13:50:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1020404375	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		f
imp-1179	cita	2026-08-14	14:00:00	14:30:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1152188224	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-118	cita	2026-06-06	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-42779460	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-30 00:00:00		f
imp-1180	cita	2026-08-14	14:30:00	15:00:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1034994995	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-1181	cita	2026-08-14	15:00:00	15:30:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1001419123	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-1182	cita	2026-08-14	16:30:00	17:15:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32353013	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		f
imp-1183	cita	2026-08-14	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32353013	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-24 00:00:00		f
imp-1184	cita	2026-08-14	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-43115783	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1185	cita	2026-08-15	09:00:00	09:30:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1128429628	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-15 00:00:00		t
imp-1186	cita	2026-08-15	09:00:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-43867018	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-25 00:00:00		f
imp-1187	cita	2026-08-15	09:30:00	10:00:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1018345520	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-15 00:00:00		t
imp-1188	cita	2026-08-15	09:30:00	10:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1037671756	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-05 00:00:00		t
imp-1189	cita	2026-08-15	10:00:00	10:30:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1037604751	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-15 00:00:00		t
imp-119	cita	2026-06-06	10:00:00	10:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-42779460	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-1190	cita	2026-08-15	10:00:00	10:30:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-43653810	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-15 00:00:00		f
imp-1191	cita	2026-08-15	10:30:00	11:00:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-43619949	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-15 00:00:00		t
imp-1192	cita	2026-08-15	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1020404375	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-15 00:00:00		t
imp-1193	cita	2026-08-15	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1020404375	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		f
imp-1194	cita	2026-08-15	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1020404375	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-14 00:00:00		f
imp-1195	cita	2026-08-15	11:00:00	11:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1053789864	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-04 00:00:00		f
imp-1196	cita	2026-08-15	11:30:00	12:00:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-diseno-de-cejas	cli-1037624943	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-15 00:00:00		t
imp-1197	cita	2026-08-15	14:00:00	14:20:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-123456789	est-confirmado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		t
imp-1198	cita	2026-08-15	14:00:00	14:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-123456789	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1199	cita	2026-08-15	14:30:00	15:15:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-22081972	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-12	cita	2026-06-03	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52965240	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-120	cita	2026-06-06	10:00:00	10:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-42779460	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-1200	cita	2026-08-15	14:30:00	15:15:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036620763	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-06 00:00:00		f
imp-1201	cita	2026-08-15	15:00:00	15:45:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-22081972	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-14 00:00:00		f
imp-1202	cita	2026-08-15	15:00:00	15:45:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-8163328	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-06 00:00:00		f
imp-1203	cita	2026-08-18	10:00:00	10:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1001534562	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-1204	cita	2026-08-18	10:30:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-1090480034	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-12 00:00:00		t
imp-1205	cita	2026-08-18	10:30:00	11:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43110114	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1206	cita	2026-08-18	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-carbon-peel	cli-1090480034	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-18 00:00:00		t
imp-1207	cita	2026-08-18	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017932526	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-18 00:00:00		t
imp-1208	cita	2026-08-18	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017932526	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-18 00:00:00		t
imp-1209	cita	2026-08-18	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-12022353	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-12 00:00:00		t
imp-121	cita	2026-06-06	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152226930	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-29 00:00:00		t
imp-1210	cita	2026-08-18	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-38942917	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-05 00:00:00		f
imp-1211	cita	2026-08-19	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1039448466	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1212	cita	2026-08-19	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21831091	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1213	cita	2026-08-19	11:00:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-1040515348	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1214	cita	2026-08-19	11:30:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-43877210	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1215	cita	2026-08-19	12:30:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1037668476	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1216	cita	2026-08-19	14:00:00	14:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1045755137	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1217	cita	2026-08-19	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1090493435	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1218	cita	2026-08-19	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-38942917	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-15 00:00:00		t
imp-1219	cita	2026-08-19	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-12022353	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-18 00:00:00		t
imp-122	cita	2026-06-06	10:00:00	11:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-52151950	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-15 00:00:00		f
imp-1220	cita	2026-08-19	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43256482	est-pendiente	Recepcionista	TESORO  CATALINA JARMILLO	nc: 11:36 am		\N	\N	t	2026-07-16 00:00:00		t
imp-1221	cita	2026-08-19	16:30:00	16:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1037668476	est-cumplido	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		t
imp-1222	cita	2026-08-20	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-12022353	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1223	cita	2026-08-20	11:00:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1020471361	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-20 00:00:00		t
imp-1224	cita	2026-08-20	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1020471361	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-20 00:00:00		t
imp-1225	cita	2026-08-20	12:00:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-63523969	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-20 00:00:00		t
imp-1226	cita	2026-08-20	12:30:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1098757306	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-20 00:00:00		t
imp-1227	cita	2026-08-20	13:00:00	13:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1128405584	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-08 00:00:00		t
imp-1228	cita	2026-08-20	14:00:00	14:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1053789864	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-14 00:00:00		f
imp-1229	cita	2026-08-20	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-1000900043	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-123	cita	2026-06-06	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-43110374	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-1230	cita	2026-08-20	15:00:00	15:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1000900043	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-1231	cita	2026-08-20	15:30:00	16:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43623570	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-1232	cita	2026-08-20	15:30:00	16:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43623570	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-27 00:00:00		f
imp-1233	cita	2026-08-20	15:30:00	16:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1128405584	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-20 00:00:00		t
imp-1234	cita	2026-08-20	15:30:00	16:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1128405584	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-20 00:00:00		f
imp-1235	cita	2026-08-20	16:00:00	16:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1020471361	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-18 00:00:00		f
imp-1236	cita	2026-08-20	16:30:00	16:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1037668476	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-23 00:00:00		f
imp-1237	cita	2026-08-21	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-43220638	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1238	cita	2026-08-21	10:00:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1041611004	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-21 00:00:00		t
imp-1239	cita	2026-08-21	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1125293826	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-22 00:00:00		f
imp-124	cita	2026-06-06	11:00:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1037578944	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-1240	cita	2026-08-21	11:00:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-123456789	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1241	cita	2026-08-21	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1125293826	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-22 00:00:00		f
imp-1242	cita	2026-08-21	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037610906	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-1243	cita	2026-08-21	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43628557	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-13 00:00:00		f
imp-1244	cita	2026-08-21	13:00:00	13:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1151953915	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-21 00:00:00		f
imp-1245	cita	2026-08-21	13:00:00	13:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1151953915	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-21 00:00:00		t
imp-1246	cita	2026-08-21	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128271946	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-31 00:00:00		t
imp-1247	cita	2026-08-21	14:30:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1006820137	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-08-21 00:00:00		t
imp-1248	cita	2026-08-21	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1094977327	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-21 00:00:00		t
imp-1249	cita	2026-08-21	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43538681	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-21 00:00:00		t
imp-125	cita	2026-06-06	11:30:00	12:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1037570796	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-1250	cita	2026-08-21	16:00:00	16:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-43971658	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-05 00:00:00		t
imp-1251	cita	2026-08-21	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42789487	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1252	cita	2026-08-21	17:30:00	18:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1006820137	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-18 00:00:00		f
imp-1253	cita	2026-08-22	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43867018	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-25 00:00:00		t
imp-1254	cita	2026-08-22	09:30:00	10:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-43867018	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-21 00:00:00		t
imp-1255	cita	2026-08-22	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-52441707	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-25 00:00:00		f
imp-1256	cita	2026-08-22	11:00:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-52441707	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-25 00:00:00		t
imp-1257	cita	2026-08-22	11:30:00	12:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-43867018	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-31 00:00:00		f
imp-1258	cita	2026-08-22	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1094977327	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-27 00:00:00		f
imp-1259	cita	2026-08-22	14:00:00	14:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-43640875	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-22 00:00:00		t
imp-126	cita	2026-06-06	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152442893	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-16 00:00:00		f
imp-1260	cita	2026-08-22	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-43640875	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-14 00:00:00		t
imp-1261	cita	2026-08-22	15:30:00	16:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-43725432	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-20 00:00:00		f
imp-1262	cita	2026-08-22	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1214739567	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-22 00:00:00		t
imp-1263	cita	2026-08-22	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-36754661	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-1264	cita	2026-08-22	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-36754661	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-21 00:00:00		t
imp-1265	cita	2026-08-24	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1125293826	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-1266	cita	2026-08-24	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1125293826	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-18 00:00:00		f
imp-1267	cita	2026-08-24	11:00:00	11:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1128405584	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-1268	cita	2026-08-24	14:00:00	14:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1053789864	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-08-20 00:00:00		f
imp-1269	cita	2026-08-24	14:30:00	15:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-55305950	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-19 00:00:00		t
imp-127	cita	2026-06-06	12:00:00	12:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1037635627	est-confirmado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		t
imp-1270	cita	2026-08-24	15:00:00	16:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-radiofrecuencia-fraccionada-alta-intensidad	cli-98562114	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-20 00:00:00		f
imp-1271	cita	2026-08-24	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-98562114	est-cancelado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-20 00:00:00		f
imp-1272	cita	2026-08-24	15:30:00	16:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-43725432	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-20 00:00:00		t
imp-1273	cita	2026-08-24	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21481522	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-1274	cita	2026-08-25	11:30:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-42982544	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-25 00:00:00		t
imp-1275	cita	2026-08-25	12:00:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1039457628	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-25 00:00:00		t
imp-1276	cita	2026-08-25	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037648065	est-pendiente	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-25 00:00:00		t
imp-1277	cita	2026-08-25	14:00:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-masaje-de-relajacion	cli-1036631947	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-25 00:00:00		t
imp-1278	cita	2026-08-25	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1130667990	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-05 00:00:00		t
imp-1279	cita	2026-08-26	12:30:00	13:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43973519	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-24 00:00:00		f
imp-128	cita	2026-06-06	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-36754661	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-1280	cita	2026-08-26	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43571311	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-12 00:00:00		t
imp-1281	cita	2026-08-26	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43571311	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-12 00:00:00		f
imp-1282	cita	2026-08-26	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1098757306	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-20 00:00:00		f
imp-1283	cita	2026-08-27	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43602238	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-06 00:00:00		f
imp-1284	cita	2026-08-27	09:30:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1002126952	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-27 00:00:00		t
imp-1285	cita	2026-08-27	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32258349	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-1286	cita	2026-08-27	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42880332	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1287	cita	2026-08-27	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42880332	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-06 00:00:00		t
imp-1288	cita	2026-08-27	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017126454	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-05 00:00:00		f
imp-1289	cita	2026-08-27	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42761330	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-26 00:00:00		t
imp-129	cita	2026-06-06	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1143148111	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-16 00:00:00		t
imp-1290	cita	2026-08-27	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43614016	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-27 00:00:00		f
imp-1291	cita	2026-08-27	13:00:00	13:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-33994336	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-26 00:00:00		f
imp-1292	cita	2026-08-27	14:00:00	14:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1053789864	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-24 00:00:00		t
imp-1293	cita	2026-08-27	15:00:00	16:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-masaje-de-relajacion	cli-1067951904	est-incumplido	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-26 00:00:00		t
imp-1294	cita	2026-08-27	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1098757306	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-26 00:00:00		t
imp-1295	cita	2026-08-27	16:30:00	17:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-123456789	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-08-26 00:00:00		f
imp-1296	cita	2026-08-27	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-123456789	est-confirmado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-26 00:00:00		t
imp-1297	cita	2026-08-27	17:30:00	18:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-123456789	est-confirmado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-26 00:00:00		t
imp-1298	cita	2026-08-29	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1121825659	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-1299	cita	2026-08-29	09:30:00	10:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1121825659	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-13	cita	2026-06-03	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52974508	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-08 00:00:00		f
imp-130	cita	2026-06-06	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037670965	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-1300	cita	2026-08-29	10:00:00	10:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52989297	est-pendiente	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		t
imp-1301	cita	2026-08-29	10:00:00	10:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1121825659	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-1302	cita	2026-08-29	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-28561811	est-pendiente	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-21 00:00:00		t
imp-1303	cita	2026-08-28	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1216406	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-08-27 00:00:00		f
imp-1304	cita	2026-08-28	12:30:00	13:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43973519	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-25 00:00:00		f
imp-1305	cita	2026-08-28	13:00:00	13:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1216406	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-28 00:00:00		t
imp-1306	cita	2026-08-28	13:30:00	14:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1216406	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-28 00:00:00		t
imp-1307	cita	2026-08-28	14:00:00	14:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-1033654796	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-28 00:00:00		f
imp-1308	cita	2026-08-29	10:00:00	10:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-22069021	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-25 00:00:00		f
imp-1309	cita	2026-08-29	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-22069021	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-25 00:00:00		f
imp-131	cita	2026-06-06	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037622259	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-1310	cita	2026-08-29	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-1037613328	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-27 00:00:00		t
imp-1311	cita	2026-08-29	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-1037613328	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-26 00:00:00		f
imp-1312	cita	2026-08-29	14:00:00	14:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-123456789	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-27 00:00:00		t
imp-1313	cita	2026-08-29	14:30:00	14:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-123456789	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-08-27 00:00:00		t
imp-1314	cita	2026-08-29	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-30712419	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-23 00:00:00		t
imp-1315	cita	2026-08-29	15:30:00	16:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-43725432	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-26 00:00:00		t
imp-1316	cita	2026-08-31	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43089123	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-29 00:00:00		t
imp-1317	cita	2026-08-31	10:30:00	10:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-32543644	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-29 00:00:00		f
imp-1318	cita	2026-08-31	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43089123	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-27 00:00:00		f
imp-1319	cita	2026-08-31	11:30:00	11:50:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-33994336	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-08-27 00:00:00		t
imp-132	cita	2026-06-06	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-36754661	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-15 00:00:00		f
imp-1320	cita	2026-08-31	12:00:00	12:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1017148290	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-31 00:00:00		t
imp-1321	cita	2026-08-31	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43614016	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-08-27 00:00:00		f
imp-1322	cita	2026-08-31	16:30:00	17:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1014872117	est-cumplido	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-08-31 00:00:00		t
imp-133	cita	2026-06-09	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42799736	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-19 00:00:00		t
imp-134	cita	2026-06-09	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42898873	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-19 00:00:00		t
imp-135	cita	2026-06-09	10:00:00	10:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1001534562	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-136	cita	2026-06-09	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152193761	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-19 00:00:00		t
imp-137	cita	2026-06-09	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037648065	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-05-19 00:00:00		f
imp-138	cita	2026-06-09	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-43110114	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-139	cita	2026-06-09	11:00:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43110114	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-14	cita	2026-06-03	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-79896515	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-07 00:00:00		t
imp-140	cita	2026-06-09	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1001588849	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-28 00:00:00		f
imp-141	cita	2026-06-09	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1001588849	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-142	cita	2026-06-09	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43110114	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-143	cita	2026-06-10	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020798300	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-144	cita	2026-06-10	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1018422925	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-145	cita	2026-06-10	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-146	cita	2026-06-10	14:30:00	15:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52974508	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-147	cita	2026-06-10	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-148	cita	2026-06-10	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-39695567	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-20 00:00:00		t
imp-149	cita	2026-06-10	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32477222	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-15	cita	2026-06-03	14:30:00	15:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-79896515	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-150	cita	2026-06-10	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1001534562	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-151	cita	2026-06-10	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1216406	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-152	cita	2026-06-10	10:00:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-42105755	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-153	cita	2026-06-10	11:00:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-32242047	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-154	cita	2026-06-10	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-30402168	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-155	cita	2026-06-10	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017929180	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-20 00:00:00		t
imp-156	cita	2026-06-11	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020798300	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-157	cita	2026-06-11	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020798300	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-158	cita	2026-06-11	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1015478534	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-159	cita	2026-06-11	09:30:00	10:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-51874849	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		f
imp-16	cita	2026-06-03	16:00:00	16:20:00	esp-martha-isabel-lopez-suarez	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1020715074	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-07 00:00:00		f
imp-160	cita	2026-06-11	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1015478534	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-161	cita	2026-06-11	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53013834	est-reprogramado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-162	cita	2026-06-11	14:00:00	14:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-163	cita	2026-06-11	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52974508	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-164	cita	2026-06-11	14:30:00	15:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		f
imp-165	cita	2026-06-11	15:00:00	15:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		f
imp-166	cita	2026-06-11	15:30:00	16:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-167	cita	2026-06-11	16:00:00	16:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-168	cita	2026-06-11	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1001534562	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-169	cita	2026-06-11	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-55305950	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-17	cita	2026-06-03	16:00:00	16:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1020715074	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-07 00:00:00		f
imp-170	cita	2026-06-11	11:00:00	12:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-1037648065	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-171	cita	2026-06-11	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43602238	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-172	cita	2026-06-11	11:30:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-66738837	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-173	cita	2026-06-11	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-carbon-peel	cli-1037648065	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-174	cita	2026-06-11	13:00:00	13:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-55305950	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-02 00:00:00		f
imp-175	cita	2026-06-11	13:00:00	13:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-55305950	est-cancelado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		f
imp-176	cita	2026-06-11	14:00:00	14:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1037635627	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		f
imp-177	cita	2026-06-11	14:00:00	14:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1037635627	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-178	cita	2026-06-11	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43017004	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-179	cita	2026-06-11	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1034294175	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-18	cita	2026-06-03	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-180	cita	2026-06-11	14:30:00	15:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-52273577	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-181	cita	2026-06-11	16:00:00	16:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-38942917	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-182	cita	2026-06-11	16:30:00	17:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1001139336	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-183	cita	2026-06-11	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-38942917	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-184	cita	2026-06-11	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21481522	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-185	cita	2026-06-11	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128276823	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-21 00:00:00		t
imp-186	cita	2026-06-11	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020798300	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-187	cita	2026-06-11	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020798300	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-188	cita	2026-06-11	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1015478534	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-189	cita	2026-06-11	09:30:00	10:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-51874849	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		f
imp-19	cita	2026-06-04	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51874849	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-07 00:00:00		f
imp-190	cita	2026-06-11	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1015478534	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-191	cita	2026-06-11	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53013834	est-reprogramado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-192	cita	2026-06-11	14:00:00	14:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-193	cita	2026-06-11	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52974508	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-194	cita	2026-06-11	14:30:00	15:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		f
imp-195	cita	2026-06-11	15:00:00	15:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		f
imp-196	cita	2026-06-11	15:30:00	16:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-197	cita	2026-06-11	16:00:00	16:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-198	cita	2026-06-12	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020798300	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-199	cita	2026-06-12	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-63499559	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-20 00:00:00		t
imp-2	cita	2026-06-01	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1018464161	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-21 00:00:00		t
imp-20	cita	2026-06-04	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1037634850	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-24 00:00:00		f
imp-200	cita	2026-06-12	10:00:00	10:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-63499559	est-realizado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-201	cita	2026-06-12	10:00:00	11:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-51874849	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		f
imp-202	cita	2026-06-12	10:30:00	11:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-63499559	est-incumplido	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-203	cita	2026-06-12	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010177070	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-204	cita	2026-06-12	11:30:00	12:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-1107069165	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-205	cita	2026-06-12	14:30:00	14:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1057710556	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-20 00:00:00		t
imp-206	cita	2026-06-12	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-207	cita	2026-06-13	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020798300	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-208	cita	2026-06-13	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-444444336	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-16 00:00:00		f
imp-209	cita	2026-06-13	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-444444336	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-13 00:00:00		t
imp-21	cita	2026-06-04	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-210	cita	2026-06-13	15:00:00	15:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1037644195	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-23 00:00:00		t
imp-211	cita	2026-06-13	15:30:00	15:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1037644195	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-23 00:00:00		t
imp-212	cita	2026-06-13	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		f
imp-213	cita	2026-06-13	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51935765	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-214	cita	2026-06-15	14:30:00	15:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52252979	est-pendiente	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-19 00:00:00		t
imp-215	cita	2026-06-11	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1001534562	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-216	cita	2026-06-11	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-55305950	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-217	cita	2026-06-11	11:00:00	12:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-1037648065	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-218	cita	2026-06-11	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43602238	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-219	cita	2026-06-11	11:30:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-66738837	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-22	cita	2026-06-04	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-24731927	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-07 00:00:00		f
imp-220	cita	2026-06-11	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-carbon-peel	cli-1037648065	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-221	cita	2026-06-11	13:00:00	13:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-55305950	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-02 00:00:00		f
imp-222	cita	2026-06-11	13:00:00	13:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-55305950	est-cancelado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		f
imp-223	cita	2026-06-11	14:00:00	14:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1037635627	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		f
imp-224	cita	2026-06-11	14:00:00	14:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1037635627	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-225	cita	2026-06-11	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43017004	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-226	cita	2026-06-11	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1034294175	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-227	cita	2026-06-11	14:30:00	15:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-52273577	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-228	cita	2026-06-11	16:00:00	16:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-38942917	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-229	cita	2026-06-11	16:30:00	17:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1001139336	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-23	cita	2026-06-04	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-24731927	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-230	cita	2026-06-11	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-38942917	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-231	cita	2026-06-11	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21481522	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-232	cita	2026-06-11	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128276823	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-21 00:00:00		t
imp-233	cita	2026-06-12	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1018447506	est-confirmado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-234	cita	2026-06-12	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43757644	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-235	cita	2026-06-12	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-123456789	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-236	cita	2026-06-12	12:30:00	13:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-38942917	est-confirmado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-237	cita	2026-06-12	13:00:00	14:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-radiofrecuencia-fraccionada-alta-intensidad	cli-123456789	est-confirmado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-238	cita	2026-06-12	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-42964420	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-239	cita	2026-06-12	15:00:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-43868433	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-24	cita	2026-06-04	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-38262991	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO	Cambio la cita de fecha		\N	\N	t	2026-05-07 00:00:00		f
imp-240	cita	2026-06-12	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43017004	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-241	cita	2026-06-12	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-42766441	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-242	cita	2026-06-12	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-63316600	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-22 00:00:00		t
imp-243	cita	2026-06-12	17:30:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-63316600	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-244	cita	2026-06-13	09:00:00	09:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1037570796	est-cumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-245	cita	2026-06-13	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1037578944	est-cumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-13 00:00:00		t
imp-246	cita	2026-06-13	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1037570796	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-247	cita	2026-06-13	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152226930	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-06 00:00:00		t
imp-248	cita	2026-06-13	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43594009	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-22 00:00:00		f
imp-249	cita	2026-06-13	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017932526	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-05-23 00:00:00		f
imp-25	cita	2026-06-04	14:30:00	15:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010218251	est-realizado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-250	cita	2026-06-13	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017932526	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-05-23 00:00:00		f
imp-251	cita	2026-06-13	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-cumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-13 00:00:00		t
imp-252	cita	2026-06-13	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1112776705	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-26 00:00:00		t
imp-253	cita	2026-06-15	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43750606	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-254	cita	2026-06-15	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-39412621	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-255	cita	2026-06-16	09:00:00	10:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-1052397670	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-29 00:00:00		t
imp-256	cita	2026-06-16	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52295932	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-257	cita	2026-06-16	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53013834	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-258	cita	2026-06-16	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1121825659	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-13 00:00:00		t
imp-259	cita	2026-06-16	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-13 00:00:00		f
imp-26	cita	2026-06-04	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1037634850	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-24 00:00:00		t
imp-260	cita	2026-06-16	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43258723	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-261	cita	2026-06-16	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037635627	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-06 00:00:00		t
imp-262	cita	2026-06-16	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1026251454	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-26 00:00:00		t
imp-263	cita	2026-06-16	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43602238	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-20 00:00:00		t
imp-264	cita	2026-06-16	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-39281547	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-265	cita	2026-06-16	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1125293826	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-21 00:00:00		t
imp-266	cita	2026-06-16	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-26 00:00:00		t
imp-267	cita	2026-06-16	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-26 00:00:00		t
imp-268	cita	2026-06-16	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037648065	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-269	cita	2026-06-16	14:00:00	14:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1152191791	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-27	cita	2026-06-05	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-38262991	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		f
imp-270	cita	2026-06-16	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037648065	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-271	cita	2026-06-16	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128474994	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-272	cita	2026-06-16	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43256482	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-273	cita	2026-06-16	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43628557	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-274	cita	2026-06-17	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020798300	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-10 00:00:00		f
imp-275	cita	2026-06-17	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-50922034	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-276	cita	2026-06-17	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52712795	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-277	cita	2026-06-17	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1001077567	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-278	cita	2026-06-17	15:30:00	16:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1001077567	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-279	cita	2026-06-17	16:30:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-xs	cli-1192768653	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-28	cita	2026-06-05	11:00:00	11:30:00	esp-martha-isabel-lopez-suarez	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1107069165	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-06 00:00:00		f
imp-280	cita	2026-06-17	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037648065	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		f
imp-281	cita	2026-06-17	10:00:00	10:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1045421615	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-16 00:00:00		t
imp-282	cita	2026-06-17	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-28561762	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-283	cita	2026-06-17	11:30:00	12:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-28561762	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-284	cita	2026-06-17	12:00:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-43976430	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-285	cita	2026-06-17	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036603493	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		f
imp-286	cita	2026-06-17	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43750606	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-13 00:00:00		t
imp-287	cita	2026-06-17	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43017003	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-12 00:00:00		f
imp-288	cita	2026-06-17	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43532117	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-14 00:00:00		t
imp-289	cita	2026-06-17	15:00:00	15:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1014872117	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-29	cita	2026-06-05	11:00:00	11:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1107069165	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-290	cita	2026-06-17	16:00:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1036648060	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-291	cita	2026-06-17	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43525709	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-22 00:00:00		f
imp-292	cita	2026-06-18	09:30:00	10:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-51874849	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		f
imp-293	cita	2026-06-18	11:30:00	12:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-53067438	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-294	cita	2026-06-18	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52252979	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-295	cita	2026-06-18	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-13 00:00:00		t
imp-296	cita	2026-06-18	16:30:00	17:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020715074	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-297	cita	2026-06-18	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-16209031	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-298	cita	2026-06-18	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-16209031	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-3	cita	2026-06-01	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-50922034	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-22 00:00:00		t
imp-30	cita	2026-06-05	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010177070	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-08 00:00:00		f
imp-300	cita	2026-06-18	15:00:00	15:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43525709	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-301	cita	2026-06-18	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43628557	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-13 00:00:00		f
imp-302	cita	2026-06-18	15:30:00	16:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43556681	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-303	cita	2026-06-18	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43602238	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-304	cita	2026-06-18	16:00:00	16:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1001139336	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-305	cita	2026-06-18	16:00:00	16:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1014872117	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-306	cita	2026-06-18	16:30:00	17:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1037668476	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		f
imp-307	cita	2026-06-18	16:30:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1037668476	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-308	cita	2026-06-18	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-52298527	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-21 00:00:00		t
imp-309	cita	2026-06-18	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128269414	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-29 00:00:00		f
imp-31	cita	2026-06-05	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53011725	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-310	cita	2026-06-18	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21396882	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-311	cita	2026-06-19	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-38262991	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-312	cita	2026-06-19	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1000953384	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-313	cita	2026-06-19	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1018500681	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-28 00:00:00		t
imp-314	cita	2026-06-19	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1105693410	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-315	cita	2026-06-19	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1121825659	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-316	cita	2026-06-19	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1121825659	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-317	cita	2026-06-19	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1000953384	est-confirmado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-318	cita	2026-06-19	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1121825659	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-319	cita	2026-06-19	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1121825659	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-32	cita	2026-06-05	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52974508	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-03 00:00:00		f
imp-320	cita	2026-06-19	14:30:00	14:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1042771641	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		f
imp-321	cita	2026-06-19	14:30:00	15:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1121825659	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-322	cita	2026-06-19	15:00:00	15:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1042771641	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		f
imp-323	cita	2026-06-19	16:30:00	16:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1042771641	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-324	cita	2026-06-19	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1000953384	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		f
imp-325	cita	2026-06-20	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1030603570	est-cancelado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-05-11 00:00:00		f
imp-326	cita	2026-06-20	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1052389892	est-cancelado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-05-11 00:00:00		f
imp-327	cita	2026-06-20	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1030593561	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		f
imp-328	cita	2026-06-20	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1030593561	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-329	cita	2026-06-20	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-33	cita	2026-06-05	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-31961068	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-11 00:00:00		f
imp-330	cita	2026-06-20	12:00:00	12:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1010148226	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-331	cita	2026-06-20	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1032406074	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-332	cita	2026-06-20	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1053811453	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		f
imp-333	cita	2026-06-20	14:30:00	15:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-1053811453	est-cancelado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-05-25 00:00:00		f
imp-334	cita	2026-06-20	15:00:00	15:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1010148226	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-335	cita	2026-06-20	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010081806	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-13 00:00:00		t
imp-336	cita	2026-06-20	16:30:00	17:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1014305681	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-337	cita	2026-06-19	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-338	cita	2026-06-19	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-41892976	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-339	cita	2026-06-19	12:00:00	12:45:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-toxina-botox	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-34	cita	2026-06-05	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-31961068	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-340	cita	2026-06-19	12:00:00	12:45:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-toxina-botox	cli-41892976	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-341	cita	2026-06-19	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21396882	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-29 00:00:00		f
imp-342	cita	2026-06-19	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-42828462	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		f
imp-343	cita	2026-06-19	15:30:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1040736835	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-344	cita	2026-06-19	15:30:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-1040736835	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-345	cita	2026-06-19	16:00:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1040515348	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-346	cita	2026-06-19	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43979089	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-347	cita	2026-06-19	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-63316600	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-348	cita	2026-06-19	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1035438745	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-29 00:00:00		f
imp-349	cita	2026-06-19	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21396882	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-35	cita	2026-06-06	09:00:00	09:30:00	esp-martha-isabel-lopez-suarez	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1024543929	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-02 00:00:00		f
imp-350	cita	2026-06-20	09:00:00	09:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1037613769	est-cancelado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-10 00:00:00		f
imp-351	cita	2026-06-20	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43867018	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-352	cita	2026-06-20	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-30712419	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		t
imp-353	cita	2026-06-20	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128264708	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-354	cita	2026-06-20	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43594009	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-355	cita	2026-06-20	11:30:00	12:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1128405584	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-356	cita	2026-06-20	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128269414	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-357	cita	2026-06-20	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43260411	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		t
imp-358	cita	2026-06-20	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036620763	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		t
imp-359	cita	2026-06-20	14:30:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-52441707	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-02 00:00:00		t
imp-36	cita	2026-06-06	09:30:00	10:00:00	esp-martha-isabel-lopez-suarez	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1024543929	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-02 00:00:00		f
imp-360	cita	2026-06-20	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128269414	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-361	cita	2026-06-20	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43878034	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-362	cita	2026-06-20	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-599953	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		f
imp-363	cita	2026-06-22	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52429996	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-15 00:00:00		f
imp-364	cita	2026-06-22	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1033722369	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-26 00:00:00		f
imp-365	cita	2026-06-22	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1125293826	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-366	cita	2026-06-22	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037648065	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-367	cita	2026-06-22	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-confirmado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		t
imp-368	cita	2026-06-22	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42888483	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		t
imp-369	cita	2026-06-22	15:00:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-1033654796	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-37	cita	2026-06-06	10:00:00	11:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-52151950	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-05-25 00:00:00		t
imp-370	cita	2026-06-22	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128269414	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		f
imp-371	cita	2026-06-22	16:00:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-1040515348	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-372	cita	2026-06-22	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43525709	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-373	cita	2026-06-22	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21481522	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-374	cita	2026-06-22	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32353013	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-375	cita	2026-06-23	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1019023831	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-15 00:00:00		f
imp-376	cita	2026-06-23	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52694094	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-26 00:00:00		f
imp-377	cita	2026-06-23	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1032427896	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-378	cita	2026-06-23	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-20627238	est-cancelado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-379	cita	2026-06-23	11:30:00	11:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52329181	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-38	cita	2026-06-06	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52151950	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-09 00:00:00		t
imp-380	cita	2026-06-23	12:00:00	12:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-52536110	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-381	cita	2026-06-23	12:30:00	13:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1022335008	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-382	cita	2026-06-23	14:00:00	14:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1024540490	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-383	cita	2026-06-23	14:00:00	14:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-26 00:00:00		t
imp-384	cita	2026-06-23	14:30:00	15:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-52983883	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-385	cita	2026-06-23	14:30:00	15:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-26 00:00:00		t
imp-386	cita	2026-06-23	14:30:00	14:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-1022335008	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-23 00:00:00		t
imp-387	cita	2026-06-23	15:00:00	15:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1053330716	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-388	cita	2026-06-23	15:30:00	16:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-53015367	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-389	cita	2026-06-23	16:00:00	16:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1015452061	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-39	cita	2026-06-06	12:00:00	12:20:00	esp-martha-isabel-lopez-suarez	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1094881949	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-02 00:00:00		f
imp-390	cita	2026-06-23	16:30:00	17:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1032423777	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-23 00:00:00		f
imp-391	cita	2026-06-23	16:30:00	17:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-30285726	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-23 00:00:00		t
imp-392	cita	2026-06-23	16:30:00	16:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52069804	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-393	cita	2026-06-23	17:00:00	17:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1032423777	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-394	cita	2026-06-23	17:00:00	17:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-30285726	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-23 00:00:00		f
imp-395	cita	2026-06-23	17:30:00	18:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-30285726	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-06 00:00:00		f
imp-396	cita	2026-06-23	18:00:00	18:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1018447506	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-12 00:00:00		f
imp-397	cita	2026-06-23	18:00:00	18:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-52791664	est-cancelado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-398	cita	2026-06-23	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-43874449	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		f
imp-399	cita	2026-06-23	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-28561762	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-20 00:00:00		f
imp-4	cita	2026-06-01	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52965240	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-05-25 00:00:00		t
imp-40	cita	2026-06-06	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1094881949	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-06 00:00:00		t
imp-400	cita	2026-06-23	11:00:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-28561762	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-20 00:00:00		f
imp-401	cita	2026-06-23	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43258723	est-pendiente	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-13 00:00:00		t
imp-402	cita	2026-06-23	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43628557	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		f
imp-403	cita	2026-06-24	09:00:00	09:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1075270783	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-404	cita	2026-06-24	09:30:00	09:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52329181	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-405	cita	2026-06-24	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1052391724	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-06 00:00:00		t
imp-406	cita	2026-06-24	10:30:00	10:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-1020798300	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		f
imp-407	cita	2026-06-24	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-42030194	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-408	cita	2026-06-24	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020798300	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-24 00:00:00		t
imp-409	cita	2026-06-24	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1026254692	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-41	cita	2026-06-06	12:00:00	12:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1094881949	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-410	cita	2026-06-24	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1019023831	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-411	cita	2026-06-24	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1026254692	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-412	cita	2026-06-24	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010214230	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-29 00:00:00		t
imp-413	cita	2026-06-24	12:00:00	12:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1015452061	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-23 00:00:00		t
imp-414	cita	2026-06-24	12:30:00	12:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52069804	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-23 00:00:00		f
imp-415	cita	2026-06-24	13:00:00	13:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1022335008	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		f
imp-416	cita	2026-06-24	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-confirmado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-417	cita	2026-06-24	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-43220638	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-20 00:00:00		f
imp-418	cita	2026-06-24	10:00:00	11:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-1000332854	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-419	cita	2026-06-24	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-43874449	est-confirmado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-42	cita	2026-06-06	12:30:00	12:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1094881949	est-cancelado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-420	cita	2026-06-24	14:00:00	14:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-123456789	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-421	cita	2026-06-24	14:30:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-123456789	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-422	cita	2026-06-24	15:00:00	15:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-49723010	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-23 00:00:00		t
imp-423	cita	2026-06-25	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1105693410	est-confirmado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-24 00:00:00		t
imp-424	cita	2026-06-25	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-pendiente	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-425	cita	2026-06-26	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53011725	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-426	cita	2026-06-26	09:30:00	10:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		f
imp-427	cita	2026-06-26	10:30:00	10:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1001854605	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		t
imp-428	cita	2026-06-26	10:30:00	10:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1001854605	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		f
imp-429	cita	2026-06-26	10:30:00	10:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1001854605	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-27 00:00:00		f
imp-43	cita	2026-06-06	12:30:00	12:50:00	esp-martha-isabel-lopez-suarez	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1094881949	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-02 00:00:00		f
imp-430	cita	2026-06-26	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-431	cita	2026-06-26	11:00:00	11:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1010177070	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-432	cita	2026-06-26	11:30:00	11:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1010177070	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		t
imp-433	cita	2026-06-26	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52024703	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		t
imp-434	cita	2026-06-26	15:30:00	16:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1050951071	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-435	cita	2026-06-26	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1102799405	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-06 00:00:00		f
imp-436	cita	2026-06-27	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-79896515	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-437	cita	2026-06-27	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52108151	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-02 00:00:00		t
imp-438	cita	2026-06-27	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010196637	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-439	cita	2026-06-27	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1022335008	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-44	cita	2026-06-06	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1102799405	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-29 00:00:00		t
imp-440	cita	2026-06-27	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53106872	est-pendiente	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO	11.33bz		\N	\N	t	2026-06-06 00:00:00		t
imp-441	cita	2026-06-25	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-29567472	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		f
imp-442	cita	2026-06-25	10:30:00	11:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-32242459	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-25 00:00:00		f
imp-443	cita	2026-06-25	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-42828462	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-444	cita	2026-06-25	11:00:00	11:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-52520940	est-confirmado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-445	cita	2026-06-25	11:30:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-29532422	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		f
imp-446	cita	2026-06-25	12:00:00	12:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-29532422	est-pendiente	Call Center	ASESOR CC 4 CATALINA JARAMILLO	crm		\N	\N	t	2026-06-17 00:00:00		t
imp-447	cita	2026-06-25	14:00:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-masaje-de-relajacion	cli-43616101	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-448	cita	2026-06-25	14:00:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-masaje-de-relajacion	cli-43616101	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-449	cita	2026-06-25	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037635627	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-24 00:00:00		t
imp-45	cita	2026-06-06	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53106872	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-06 00:00:00		t
imp-450	cita	2026-06-25	15:30:00	16:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1128458678	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-451	cita	2026-06-25	15:30:00	16:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1128458678	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-10 00:00:00		f
imp-452	cita	2026-06-25	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036603493	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-453	cita	2026-06-25	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037635627	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-454	cita	2026-06-25	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-37841567	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-455	cita	2026-06-25	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-13873460	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-456	cita	2026-06-26	09:00:00	09:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-41892976	est-confirmado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		t
imp-457	cita	2026-06-26	10:00:00	10:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-41892976	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-458	cita	2026-06-26	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43220638	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-05-22 00:00:00		f
imp-459	cita	2026-06-26	10:30:00	11:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1013612199	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-05-22 00:00:00		f
imp-46	cita	2026-06-06	16:30:00	16:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1020715074	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-460	cita	2026-06-26	11:00:00	11:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43080476	est-confirmado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-461	cita	2026-06-26	11:30:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1017150439	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-462	cita	2026-06-26	12:00:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-63523969	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-463	cita	2026-06-26	12:30:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-444444388	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-464	cita	2026-06-26	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1094977327	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-465	cita	2026-06-26	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128271946	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-466	cita	2026-06-26	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037670965	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-467	cita	2026-06-26	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-599953	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-468	cita	2026-06-26	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-123456789	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		f
imp-469	cita	2026-06-26	16:30:00	17:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-123456789	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		f
imp-47	cita	2026-06-06	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1000575719	est-cancelado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-05-25 00:00:00		f
imp-470	cita	2026-06-26	17:00:00	17:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-123456789	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		f
imp-471	cita	2026-06-26	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037620783	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-24 00:00:00		f
imp-472	cita	2026-06-26	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037620783	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-24 00:00:00		t
imp-473	cita	2026-06-27	09:00:00	09:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43640875	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-16 00:00:00		f
imp-474	cita	2026-06-27	09:30:00	09:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-43640875	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-16 00:00:00		f
imp-475	cita	2026-06-27	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		f
imp-476	cita	2026-06-27	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-1128441518	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-477	cita	2026-06-27	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128271946	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-478	cita	2026-06-27	14:00:00	14:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1034995289	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		t
imp-479	cita	2026-06-27	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037670965	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-06 00:00:00		f
imp-48	cita	2026-06-09	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1018422925	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-480	cita	2026-06-27	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-27 00:00:00		f
imp-481	cita	2026-06-27	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43567026	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-05-23 00:00:00		f
imp-482	cita	2026-06-27	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43506547	est-pendiente	Recepcionista	TESORO  CATALINA JARMILLO	crm		\N	\N	t	2026-05-30 00:00:00		t
imp-483	cita	2026-06-27	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-311092	est-pendiente	Recepcionista	TESORO  CATALINA JARMILLO	crm		\N	\N	t	2026-05-30 00:00:00		t
imp-484	cita	2026-06-27	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1102799405	est-confirmado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		t
imp-485	cita	2026-06-30	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52694094	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-486	cita	2026-06-30	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1016094687	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-487	cita	2026-06-30	10:30:00	10:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-32780120	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		t
imp-488	cita	2026-06-30	11:00:00	11:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-32780120	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		t
imp-489	cita	2026-06-30	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010218251	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-49	cita	2026-06-09	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-40411225	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-13 00:00:00		t
imp-490	cita	2026-06-30	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1102840319	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-25 00:00:00		f
imp-491	cita	2026-06-30	12:30:00	13:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-25 00:00:00		f
imp-492	cita	2026-06-30	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53001656	est-realizado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-493	cita	2026-06-30	14:30:00	15:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-494	cita	2026-06-30	15:00:00	15:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-realizado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-495	cita	2026-06-30	15:30:00	16:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-39791787	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		f
imp-496	cita	2026-06-30	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42799736	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-497	cita	2026-06-30	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32477222	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-10 00:00:00		f
imp-498	cita	2026-06-30	10:00:00	10:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-43251799	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-13 00:00:00		f
imp-499	cita	2026-06-30	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43251799	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-13 00:00:00		f
imp-5	cita	2026-06-01	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-39721468	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-11 00:00:00		t
imp-50	cita	2026-06-09	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-20387333	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-500	cita	2026-06-30	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152193761	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		f
imp-501	cita	2026-06-30	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1094977327	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		t
imp-502	cita	2026-06-30	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152193761	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-27 00:00:00		t
imp-503	cita	2026-06-30	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-8163328	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-30 00:00:00		f
imp-504	cita	2026-06-30	13:00:00	13:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-37444430	est-confirmado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-29 00:00:00		t
imp-505	cita	2026-06-30	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-355724	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-506	cita	2026-06-30	15:00:00	15:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1034991123	est-confirmado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		t
imp-507	cita	2026-06-30	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43205728	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-26 00:00:00		f
imp-508	cita	2026-07-01	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1018422925	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-10 00:00:00		f
imp-509	cita	2026-07-01	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51951488	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-51	cita	2026-06-09	15:30:00	16:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-20387333	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-510	cita	2026-07-01	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-511	cita	2026-07-01	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-512	cita	2026-07-01	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-40411225	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-513	cita	2026-07-01	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53106872	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-514	cita	2026-07-02	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51874849	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-515	cita	2026-07-02	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1015478534	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-11 00:00:00		f
imp-516	cita	2026-07-02	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51561728	est-realizado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-517	cita	2026-07-03	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-35525646	est-incumplido	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-518	cita	2026-07-03	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-35525646	est-cancelado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-519	cita	2026-07-03	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-63499559	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		f
imp-52	cita	2026-06-09	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-09 00:00:00		t
imp-520	cita	2026-07-03	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-carbon-peel	cli-1052397670	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-29 00:00:00		t
imp-521	cita	2026-07-03	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1052397670	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-29 00:00:00		f
imp-522	cita	2026-07-03	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1032460058	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-523	cita	2026-07-03	12:00:00	12:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1107069165	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-524	cita	2026-07-03	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-31961068	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		f
imp-525	cita	2026-07-03	14:30:00	15:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-26441599	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-526	cita	2026-07-03	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1032460058	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-527	cita	2026-07-03	15:30:00	16:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-21087900	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-528	cita	2026-07-03	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-03 00:00:00		t
imp-529	cita	2026-07-04	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1024543929	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-53	cita	2026-06-01	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21395278	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		t
imp-530	cita	2026-07-04	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-444444336	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-13 00:00:00		f
imp-531	cita	2026-07-04	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1022341860	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-13 00:00:00		t
imp-532	cita	2026-07-04	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1019111289	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-03 00:00:00		f
imp-533	cita	2026-07-04	12:00:00	12:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1014305681	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-04 00:00:00		t
imp-534	cita	2026-07-04	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-535	cita	2026-07-06	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53177401	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-536	cita	2026-07-06	15:00:00	16:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-1015395409	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		t
imp-537	cita	2026-07-06	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1015395409	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		t
imp-538	cita	2026-07-07	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51874849	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-539	cita	2026-07-07	10:00:00	10:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020758898	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-28 00:00:00		t
imp-54	cita	2026-06-01	09:00:00	09:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-42057470	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-27 00:00:00		t
imp-540	cita	2026-07-07	10:30:00	11:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020758898	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-28 00:00:00		t
imp-541	cita	2026-07-07	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-50922034	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-542	cita	2026-07-07	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-07 00:00:00		t
imp-543	cita	2026-07-07	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-24731927	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		f
imp-544	cita	2026-07-07	13:00:00	13:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1000461276	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-07 00:00:00		t
imp-545	cita	2026-07-07	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52252979	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-546	cita	2026-07-07	15:30:00	16:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-547	cita	2026-07-07	16:00:00	16:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1141520024	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-548	cita	2026-07-07	16:30:00	17:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1141520024	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-549	cita	2026-07-08	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-43869520	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-55	cita	2026-06-01	10:00:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-22081972	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-550	cita	2026-07-08	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-20387333	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-551	cita	2026-07-09	10:00:00	10:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-32780120	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-27 00:00:00		f
imp-552	cita	2026-07-09	10:30:00	10:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-32780120	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-27 00:00:00		f
imp-553	cita	2026-07-09	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020756814	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-04 00:00:00		t
imp-554	cita	2026-07-09	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-50922034	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-06 00:00:00		f
imp-555	cita	2026-07-09	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-24731927	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-556	cita	2026-07-09	13:00:00	13:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52712795	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-557	cita	2026-07-09	14:00:00	14:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1141520024	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-558	cita	2026-07-09	14:30:00	15:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1141520024	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-559	cita	2026-07-09	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-50922034	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-56	cita	2026-06-01	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-43035312	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-560	cita	2026-07-09	15:30:00	16:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1018456833	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-561	cita	2026-07-09	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1019111289	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-03 00:00:00		t
imp-562	cita	2026-07-09	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-05 00:00:00		t
imp-563	cita	2026-07-10	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1121825659	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-564	cita	2026-07-10	09:30:00	09:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1121825659	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-565	cita	2026-07-10	10:00:00	10:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1121825659	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-566	cita	2026-07-10	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1015478534	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-567	cita	2026-07-10	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52295932	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-568	cita	2026-07-10	11:30:00	12:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020758898	est-cancelado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-569	cita	2026-07-10	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1020758898	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-57	cita	2026-06-01	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-35459410	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-05-25 00:00:00		t
imp-570	cita	2026-07-10	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1000953384	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-571	cita	2026-07-10	14:30:00	15:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1018500681	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-572	cita	2026-07-10	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52712795	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-573	cita	2026-07-11	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020715074	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-574	cita	2026-07-11	09:30:00	10:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020798300	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		t
imp-575	cita	2026-07-11	10:00:00	11:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-1052397670	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-576	cita	2026-07-11	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52151950	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-06 00:00:00		t
imp-577	cita	2026-07-11	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-578	cita	2026-07-11	12:30:00	12:50:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1037644195	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		t
imp-579	cita	2026-07-11	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51935765	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		t
imp-58	cita	2026-06-01	11:00:00	11:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-43907401	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-29 00:00:00		t
imp-580	cita	2026-07-13	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1019087089	est-pendiente	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-581	cita	2026-07-14	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1018500681	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-582	cita	2026-07-14	13:00:00	13:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-26441599	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-583	cita	2026-07-14	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52108151	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-584	cita	2026-07-14	16:00:00	16:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1057710556	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-585	cita	2026-07-14	16:00:00	16:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-xs	cli-1057710556	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-12 00:00:00		f
imp-586	cita	2026-07-15	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1020758898	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-587	cita	2026-07-15	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1020758898	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		t
imp-588	cita	2026-07-15	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53015367	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-589	cita	2026-07-15	16:00:00	16:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1057710556	est-reprogramado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-59	cita	2026-06-01	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1121926043	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-05-31 00:00:00		f
imp-590	cita	2026-07-16	09:00:00	09:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52069804	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-591	cita	2026-07-16	09:30:00	10:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-consulta-medica	cli-52417541	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		f
imp-592	cita	2026-07-16	09:30:00	10:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-consulta-medica	cli-52417541	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		f
imp-593	cita	2026-07-16	09:30:00	10:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-consulta-medica	cli-52417541	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		f
imp-594	cita	2026-07-16	09:30:00	09:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52417541	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		f
imp-595	cita	2026-07-16	10:00:00	10:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52069804	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-596	cita	2026-07-16	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-63335205	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-597	cita	2026-07-16	11:00:00	11:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-32780120	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-598	cita	2026-07-16	11:00:00	11:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-32780120	est-incumplido	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-599	cita	2026-07-16	11:30:00	12:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-32780120	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-6	cita	2026-06-01	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1016094687	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-60	cita	2026-06-01	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1121926043	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-600	cita	2026-07-16	12:00:00	12:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-32780120	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-601	cita	2026-07-16	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-63335205	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-602	cita	2026-07-16	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-39695567	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-10 00:00:00		f
imp-603	cita	2026-07-16	17:30:00	18:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-consulta-medica	cli-52791664	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-604	cita	2026-07-17	10:00:00	10:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52069804	est-cancelado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-605	cita	2026-07-17	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-24228735	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-606	cita	2026-07-17	11:00:00	11:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52417541	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-607	cita	2026-07-17	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-incumplido	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-608	cita	2026-07-17	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-35198555	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-609	cita	2026-07-17	15:00:00	15:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52983883	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-61	cita	2026-06-01	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-16209031	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-21 00:00:00		f
imp-610	cita	2026-07-17	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1000953384	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-611	cita	2026-07-17	17:00:00	17:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1015407135	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-612	cita	2026-07-17	17:30:00	18:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-52937855	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-613	cita	2026-07-18	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1121825659	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-614	cita	2026-07-18	09:00:00	09:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52496376	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-615	cita	2026-07-18	09:00:00	09:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52496376	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-616	cita	2026-07-18	09:30:00	09:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52791664	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		t
imp-617	cita	2026-07-18	09:30:00	10:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-consulta-medica	cli-52791664	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-618	cita	2026-07-18	09:30:00	10:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1024543929	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-03 00:00:00		t
imp-619	cita	2026-07-18	10:00:00	10:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1121825659	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-62	cita	2026-06-01	11:30:00	12:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-43035312	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-620	cita	2026-07-18	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-41952188	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-621	cita	2026-07-18	10:30:00	10:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52989297	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		f
imp-622	cita	2026-07-18	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-consulta-medica	cli-1018415797	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-18 00:00:00		t
imp-623	cita	2026-07-18	10:30:00	11:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1121825659	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-624	cita	2026-07-18	11:00:00	11:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-52546874	est-confirmado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		t
imp-625	cita	2026-07-18	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1077034356	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-626	cita	2026-07-18	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010196637	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-27 00:00:00		f
imp-627	cita	2026-07-18	12:00:00	12:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-cita-de-control-medico	cli-123456789	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		f
imp-628	cita	2026-07-18	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020715074	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-629	cita	2026-07-18	12:00:00	12:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-bogota	srv-remocion-micropigmentacion-1-sesion	cli-1030613205	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		t
imp-63	cita	2026-06-01	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-16209031	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-630	cita	2026-07-18	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010196637	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-631	cita	2026-07-18	13:00:00	13:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1077034356	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-632	cita	2026-07-18	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010196637	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-633	cita	2026-07-18	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1082856396	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-634	cita	2026-07-21	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1019023831	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-24 00:00:00		f
imp-635	cita	2026-07-21	13:00:00	13:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1023916448	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-636	cita	2026-07-21	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53106872	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-637	cita	2026-07-22	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1020798300	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-24 00:00:00		f
imp-638	cita	2026-07-22	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1026254692	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-24 00:00:00		f
imp-639	cita	2026-07-22	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1020758898	est-pendiente	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		t
imp-64	cita	2026-06-01	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-16209031	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-640	cita	2026-07-22	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1077034356	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-641	cita	2026-07-22	13:00:00	13:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-79896515	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		f
imp-642	cita	2026-07-23	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51561728	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-02 00:00:00		f
imp-643	cita	2026-07-23	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-21087900	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-03 00:00:00		f
imp-644	cita	2026-07-24	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1050951071	est-reprogramado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-06-26 00:00:00		f
imp-645	cita	2026-07-24	09:30:00	10:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020798300	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		f
imp-646	cita	2026-07-24	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1102799405	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-647	cita	2026-07-24	15:30:00	16:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-1053811453	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-29 00:00:00		f
imp-648	cita	2026-07-25	12:00:00	12:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1094881949	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-06 00:00:00		f
imp-649	cita	2026-07-25	12:30:00	13:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1094881949	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-06 00:00:00		f
imp-65	cita	2026-06-01	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037648065	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-650	cita	2026-07-28	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-07 00:00:00		f
imp-651	cita	2026-07-28	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53001656	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		f
imp-652	cita	2026-07-28	14:00:00	14:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		f
imp-653	cita	2026-07-28	14:30:00	15:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		f
imp-654	cita	2026-07-29	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1001077567	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		f
imp-655	cita	2026-07-29	14:00:00	14:20:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-s	cli-1042771641	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-656	cita	2026-07-29	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1019111289	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-657	cita	2026-07-30	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010177070	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-658	cita	2026-07-30	12:00:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010177070	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-21 00:00:00		f
imp-659	cita	2026-07-30	12:30:00	13:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		f
imp-66	cita	2026-06-01	15:00:00	15:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43110114	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-14 00:00:00		f
imp-660	cita	2026-07-30	13:00:00	13:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		f
imp-661	cita	2026-07-30	16:30:00	17:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1020715074	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-662	cita	2026-07-31	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53177401	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		f
imp-663	cita	2026-07-31	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52426985	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-23 00:00:00		f
imp-664	cita	2026-07-31	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52712795	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-665	cita	2026-07-01	10:00:00	10:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-43251799	est-cumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-666	cita	2026-07-01	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43251799	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-667	cita	2026-07-01	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017932526	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-668	cita	2026-07-01	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-8163328	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-669	cita	2026-07-01	14:00:00	14:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1216406	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-67	cita	2026-06-01	15:00:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1093801735	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-670	cita	2026-07-01	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036603493	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		f
imp-671	cita	2026-07-01	14:00:00	14:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-43743970	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-672	cita	2026-07-01	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-1033181939	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		f
imp-673	cita	2026-07-01	15:00:00	15:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1034991123	est-cumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-674	cita	2026-07-01	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036603493	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-675	cita	2026-07-01	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037635627	est-cumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-676	cita	2026-07-02	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1002558907	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		f
imp-677	cita	2026-07-02	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017932526	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-678	cita	2026-07-02	11:30:00	12:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-355724	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		f
imp-679	cita	2026-07-02	11:30:00	12:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-355724	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-68	cita	2026-06-01	15:30:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-42827722	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-680	cita	2026-07-02	13:30:00	14:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1128266791	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-29 00:00:00		t
imp-681	cita	2026-07-02	13:30:00	14:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1128266791	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-29 00:00:00		f
imp-682	cita	2026-07-02	14:00:00	14:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1037608047	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		f
imp-683	cita	2026-07-02	14:00:00	14:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43571311	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-684	cita	2026-07-02	14:00:00	14:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-43080476	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-26 00:00:00		f
imp-685	cita	2026-07-02	14:00:00	14:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43491005	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-686	cita	2026-07-02	14:00:00	14:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1128266791	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-29 00:00:00		f
imp-687	cita	2026-07-02	14:30:00	14:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1036607047	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-688	cita	2026-07-02	14:30:00	14:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1037608047	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-689	cita	2026-07-02	14:30:00	15:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1128266791	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-29 00:00:00		f
imp-69	cita	2026-06-01	16:00:00	17:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-123456789	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		t
imp-690	cita	2026-07-02	15:00:00	15:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-43080476	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-26 00:00:00		f
imp-691	cita	2026-07-02	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42883048	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-24 00:00:00		f
imp-692	cita	2026-07-02	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42883048	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-24 00:00:00		t
imp-693	cita	2026-07-02	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42883048	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-694	cita	2026-07-02	16:30:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1020493425	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-695	cita	2026-07-02	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-38942917	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-696	cita	2026-07-02	17:00:00	17:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1036607047	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-697	cita	2026-07-02	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-27 00:00:00		f
imp-698	cita	2026-07-03	09:00:00	09:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43080476	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-699	cita	2026-07-03	10:00:00	10:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1000900043	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-03 00:00:00		f
imp-7	cita	2026-06-02	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-incumplido	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-05-13 00:00:00		t
imp-70	cita	2026-06-01	16:00:00	17:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-123456789	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		f
imp-700	cita	2026-07-03	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43167251	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-701	cita	2026-07-03	11:00:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1013612199	est-incumplido	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		t
imp-702	cita	2026-07-03	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43628557	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-22 00:00:00		f
imp-703	cita	2026-07-03	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42789487	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-704	cita	2026-07-03	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42789487	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-705	cita	2026-07-04	09:00:00	09:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43640875	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-706	cita	2026-07-04	09:30:00	09:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-43640875	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-707	cita	2026-07-04	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		t
imp-708	cita	2026-07-04	10:00:00	10:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1000900043	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-03 00:00:00		f
imp-709	cita	2026-07-04	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152442893	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-71	cita	2026-06-01	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21481522	est-confirmado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-05-25 00:00:00		t
imp-710	cita	2026-07-04	11:00:00	11:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1000900043	est-cancelado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-04 00:00:00		f
imp-711	cita	2026-07-04	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1035438745	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-712	cita	2026-07-06	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43533913	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-20 00:00:00		f
imp-713	cita	2026-07-06	09:00:00	09:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-42868110	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-26 00:00:00		t
imp-714	cita	2026-07-06	10:00:00	10:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-42888483	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-715	cita	2026-07-06	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-39412621	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-02 00:00:00		f
imp-716	cita	2026-07-06	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1039448466	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-717	cita	2026-07-06	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21831091	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-718	cita	2026-07-06	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017126454	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-719	cita	2026-07-06	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1017133484	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-72	cita	2026-06-01	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21481522	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		f
imp-720	cita	2026-07-06	12:00:00	12:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-123456789	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-721	cita	2026-07-06	12:00:00	12:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-123456789	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-722	cita	2026-07-06	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1121926043	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-723	cita	2026-07-06	12:00:00	12:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1085277604	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-724	cita	2026-07-06	12:30:00	13:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43602238	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-725	cita	2026-07-06	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-726	cita	2026-07-06	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-727	cita	2026-07-06	17:00:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1046666281	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-728	cita	2026-07-06	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-30402168	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-03 00:00:00		f
imp-729	cita	2026-07-07	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43628557	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-03 00:00:00		t
imp-73	cita	2026-06-02	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-29567472	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-05-29 00:00:00		f
imp-730	cita	2026-07-07	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-51874849	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-06 00:00:00		f
imp-731	cita	2026-07-07	10:00:00	10:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43110114	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		f
imp-732	cita	2026-07-07	10:30:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1046666281	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-07 00:00:00		t
imp-733	cita	2026-07-07	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		f
imp-734	cita	2026-07-07	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		f
imp-735	cita	2026-07-07	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32258349	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-736	cita	2026-07-08	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42799736	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-737	cita	2026-07-08	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1026251454	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-738	cita	2026-07-08	10:30:00	11:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43110114	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-06 00:00:00		f
imp-739	cita	2026-07-08	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32258349	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-07 00:00:00		t
imp-74	cita	2026-06-02	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32258349	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-740	cita	2026-07-08	14:00:00	14:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43571311	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-741	cita	2026-07-08	14:00:00	14:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43571311	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-742	cita	2026-07-09	11:30:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-64584341	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-743	cita	2026-07-09	12:00:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1034294175	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-744	cita	2026-07-09	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32258349	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-745	cita	2026-07-09	14:00:00	14:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-33994336	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-08 00:00:00		f
imp-746	cita	2026-07-09	15:00:00	15:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1085277604	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-04 00:00:00		t
imp-747	cita	2026-07-09	15:30:00	15:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1013612199	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-748	cita	2026-07-09	15:30:00	16:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-38942917	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-27 00:00:00		t
imp-749	cita	2026-07-09	16:00:00	16:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1090378631	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-75	cita	2026-06-02	10:30:00	11:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43089123	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-26 00:00:00		t
imp-750	cita	2026-07-09	16:30:00	17:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1004999021	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-751	cita	2026-07-10	09:00:00	09:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1036627387	est-pendiente	Call Center	ASESOR CC 3 CATALINA JARAMILLO	no se encuentra en servicio		\N	\N	t	2026-07-07 00:00:00		t
imp-752	cita	2026-07-10	09:30:00	10:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43986250	est-pendiente	Call Center	ASESOR CC 3 CATALINA JARAMILLO	crm		\N	\N	t	2026-07-07 00:00:00		t
imp-753	cita	2026-07-10	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32257323	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-05 00:00:00		f
imp-754	cita	2026-07-10	10:00:00	10:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1046907474	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		t
imp-755	cita	2026-07-10	10:30:00	11:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1001534562	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		t
imp-756	cita	2026-07-10	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037648065	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-757	cita	2026-07-10	11:30:00	12:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43109347	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-24 00:00:00		t
imp-758	cita	2026-07-10	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1137978165	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-759	cita	2026-07-10	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128276823	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		t
imp-76	cita	2026-06-02	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32258349	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-27 00:00:00		f
imp-760	cita	2026-07-10	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21396882	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		t
imp-761	cita	2026-07-10	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-63316600	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-19 00:00:00		f
imp-762	cita	2026-07-10	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-52298527	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-763	cita	2026-07-11	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1020413179	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-11 00:00:00		t
imp-764	cita	2026-07-11	09:30:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1020413179	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-11 00:00:00		t
imp-765	cita	2026-07-11	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-29567472	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-24 00:00:00		t
imp-766	cita	2026-07-11	10:00:00	10:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-43089021	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-07 00:00:00		t
imp-767	cita	2026-07-11	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43535108	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-768	cita	2026-07-11	11:00:00	11:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43109347	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-11 00:00:00		f
imp-769	cita	2026-07-11	11:00:00	11:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-123456789	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-04 00:00:00		f
imp-77	cita	2026-06-02	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32258349	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-27 00:00:00		f
imp-770	cita	2026-07-11	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1016092066	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-771	cita	2026-07-11	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-36754661	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		t
imp-772	cita	2026-07-11	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-22081972	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-04 00:00:00		t
imp-773	cita	2026-07-11	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1000900043	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-774	cita	2026-07-11	11:30:00	12:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1000900043	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		t
imp-775	cita	2026-07-11	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32257323	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-776	cita	2026-07-11	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152211441	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-777	cita	2026-07-11	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-1037613328	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-778	cita	2026-07-11	14:00:00	14:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-123456789	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-11 00:00:00		t
imp-779	cita	2026-07-11	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43869810	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-78	cita	2026-06-02	14:30:00	15:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-123456789	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		f
imp-780	cita	2026-07-11	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43869810	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-781	cita	2026-07-11	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43869810	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-782	cita	2026-07-11	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1112776705	est-incumplido	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-783	cita	2026-07-11	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43878034	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-21 00:00:00		t
imp-784	cita	2026-07-11	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037622259	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		f
imp-785	cita	2026-07-11	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037604025	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-09 00:00:00		t
imp-786	cita	2026-07-14	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1020413179	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		f
imp-787	cita	2026-07-14	09:30:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1020413179	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		f
imp-788	cita	2026-07-14	10:30:00	11:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43110114	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-07 00:00:00		t
imp-789	cita	2026-07-14	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42888483	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		f
imp-79	cita	2026-06-02	14:30:00	15:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-123456789	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-05-30 00:00:00		f
imp-790	cita	2026-07-14	14:00:00	14:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1093801735	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-791	cita	2026-07-14	14:30:00	15:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1038105046	est-incumplido	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-792	cita	2026-07-14	15:00:00	15:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1015427858	est-incumplido	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-793	cita	2026-07-14	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43538681	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		t
imp-794	cita	2026-07-14	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-30402168	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-06 00:00:00		f
imp-795	cita	2026-07-14	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1034999825	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-11 00:00:00		t
imp-796	cita	2026-07-14	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43205728	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-797	cita	2026-07-15	09:00:00	09:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1128474994	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-798	cita	2026-07-15	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128474994	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-799	cita	2026-07-15	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43750606	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		f
imp-8	cita	2026-06-02	15:30:00	16:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52108151	est-realizado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-02 00:00:00		t
imp-80	cita	2026-06-02	15:00:00	16:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-123456789	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-800	cita	2026-07-15	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-28561762	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-801	cita	2026-07-15	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-24228735	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-802	cita	2026-07-15	11:30:00	12:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-28561762	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-803	cita	2026-07-15	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-1000900043	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-804	cita	2026-07-15	14:30:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43532117	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-805	cita	2026-07-15	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-32295764	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-806	cita	2026-07-15	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1002558907	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-807	cita	2026-07-15	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-52298527	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-808	cita	2026-07-15	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017929180	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		t
imp-809	cita	2026-07-15	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43256482	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-81	cita	2026-06-03	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152199414	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-24 00:00:00		f
imp-810	cita	2026-07-16	10:00:00	10:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-43567026	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-811	cita	2026-07-16	10:00:00	10:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1001534562	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-812	cita	2026-07-16	10:30:00	10:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-35198555	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-813	cita	2026-07-16	10:30:00	11:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43272513	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-814	cita	2026-07-16	10:30:00	10:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-43567026	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		f
imp-815	cita	2026-07-16	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1001447106	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-816	cita	2026-07-16	11:00:00	11:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-43567026	est-incumplido	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-817	cita	2026-07-16	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1001447106	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-818	cita	2026-07-16	12:00:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-66738837	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-819	cita	2026-07-16	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1043435034	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-82	cita	2026-06-03	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43167251	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-26 00:00:00		t
imp-820	cita	2026-07-16	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43869810	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-821	cita	2026-07-16	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43538681	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-822	cita	2026-07-16	14:30:00	15:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1151953915	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-823	cita	2026-07-16	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42979373	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		f
imp-824	cita	2026-07-16	16:00:00	16:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-123456789	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		t
imp-825	cita	2026-07-16	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-43115783	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-826	cita	2026-07-16	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128269414	est-pendiente	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-827	cita	2026-07-17	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1011393950	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-828	cita	2026-07-17	09:30:00	10:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43602238	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-829	cita	2026-07-17	09:30:00	10:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43602238	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-83	cita	2026-06-03	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-29567472	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-830	cita	2026-07-17	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1001447106	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-831	cita	2026-07-17	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1001447106	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-832	cita	2026-07-17	11:30:00	11:50:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-33994336	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		f
imp-833	cita	2026-07-17	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43750606	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-834	cita	2026-07-17	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-30402168	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-11 00:00:00		t
imp-835	cita	2026-07-17	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1000534795	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-836	cita	2026-07-17	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1000441777	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-837	cita	2026-07-17	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1220471144	est-cancelado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		f
imp-838	cita	2026-07-17	16:30:00	17:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1017156452	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-839	cita	2026-07-17	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-52298527	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-84	cita	2026-06-03	11:00:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43571311	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-05-27 00:00:00		f
imp-840	cita	2026-07-17	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1007622305	est-confirmado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		t
imp-841	cita	2026-07-17	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32353013	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		f
imp-842	cita	2026-07-18	09:00:00	09:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1035862006	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-843	cita	2026-07-18	09:00:00	09:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1035862006	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		f
imp-844	cita	2026-07-18	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21778111	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-845	cita	2026-07-18	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-52441707	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-20 00:00:00		f
imp-846	cita	2026-07-18	11:00:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-52441707	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-20 00:00:00		f
imp-847	cita	2026-07-18	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-1000900043	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-848	cita	2026-07-18	12:00:00	12:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1017156452	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-849	cita	2026-07-18	12:00:00	12:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1017156452	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-85	cita	2026-06-03	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1001481129	est-confirmado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-13 00:00:00		t
imp-850	cita	2026-07-18	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43869810	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-851	cita	2026-07-18	12:30:00	13:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1036635136	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-852	cita	2026-07-18	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-1036635136	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-853	cita	2026-07-18	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43869810	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-854	cita	2026-07-18	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017932526	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-855	cita	2026-07-18	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036620763	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-20 00:00:00		f
imp-856	cita	2026-07-18	14:30:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1152465203	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-857	cita	2026-07-18	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036620763	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-858	cita	2026-07-18	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1000534795	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-859	cita	2026-07-18	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1000441777	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-86	cita	2026-06-03	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-carbon-peel	cli-123456789	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-01 00:00:00		t
imp-860	cita	2026-07-18	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-8163328	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-861	cita	2026-07-18	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42789487	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-862	cita	2026-07-18	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-52298527	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-863	cita	2026-07-21	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017932526	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-21 00:00:00		t
imp-864	cita	2026-07-21	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-8163328	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-865	cita	2026-07-21	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32353013	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-866	cita	2026-07-21	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43538681	est-realizado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-867	cita	2026-07-22	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-30712419	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		t
imp-868	cita	2026-07-22	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42824198	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-21 00:00:00		t
imp-869	cita	2026-07-22	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-43840585	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-87	cita	2026-06-03	13:30:00	14:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1001481129	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-02 00:00:00		t
imp-870	cita	2026-07-22	10:00:00	10:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-43567026	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-871	cita	2026-07-22	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1125293826	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-872	cita	2026-07-22	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1115087263	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-22 00:00:00		t
imp-873	cita	2026-07-22	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-222222222	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-22 00:00:00		f
imp-874	cita	2026-07-22	13:00:00	13:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-123456789	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		f
imp-875	cita	2026-07-22	13:00:00	13:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-123456789	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-22 00:00:00		t
imp-876	cita	2026-07-22	13:30:00	13:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1017133484	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-877	cita	2026-07-22	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43750606	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		t
imp-878	cita	2026-07-22	15:00:00	15:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-123456789	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-22 00:00:00		f
imp-879	cita	2026-07-22	15:30:00	16:00:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-43089021	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-16 00:00:00		t
imp-88	cita	2026-06-03	14:00:00	14:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-1018419501	est-confirmado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-06-02 00:00:00		t
imp-880	cita	2026-07-22	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32353013	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		f
imp-881	cita	2026-07-22	16:00:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-1040515348	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-882	cita	2026-07-22	16:30:00	16:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1128448142	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-15 00:00:00		t
imp-883	cita	2026-07-23	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-30712419	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-21 00:00:00		f
imp-884	cita	2026-07-23	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-30712419	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-23 00:00:00		t
imp-885	cita	2026-07-23	14:00:00	14:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-43556681	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-18 00:00:00		f
imp-886	cita	2026-07-23	14:30:00	15:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-39412621	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-887	cita	2026-07-23	15:00:00	15:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-53051254	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-14 00:00:00		t
imp-888	cita	2026-07-23	16:30:00	16:50:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1037668476	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-18 00:00:00		t
imp-889	cita	2026-07-23	17:00:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1130620215	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-23 00:00:00		t
imp-89	cita	2026-06-03	14:00:00	14:20:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-43571311	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-02 00:00:00		t
imp-890	cita	2026-07-23	17:30:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-42964420	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-23 00:00:00		t
imp-891	cita	2026-07-24	09:00:00	09:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1037668476	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-24 00:00:00		t
imp-892	cita	2026-07-24	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1045421615	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-17 00:00:00		t
imp-893	cita	2026-07-24	10:00:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-42964420	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-24 00:00:00		t
imp-894	cita	2026-07-24	10:30:00	11:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-974407	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-24 00:00:00		t
imp-895	cita	2026-07-24	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128271946	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-26 00:00:00		f
imp-896	cita	2026-07-24	15:00:00	15:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-32299041	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-24 00:00:00		t
imp-897	cita	2026-07-24	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32353013	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-23 00:00:00		t
imp-898	cita	2026-07-24	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-8089948	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-18 00:00:00		t
imp-899	cita	2026-07-24	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32353013	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-22 00:00:00		f
imp-9	cita	2026-06-02	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52108151	est-cancelado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-06-02 00:00:00		f
imp-90	cita	2026-06-03	14:00:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-123456789	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-06-02 00:00:00		t
imp-900	cita	2026-07-25	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43867018	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-901	cita	2026-07-25	09:30:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1152465203	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-18 00:00:00		t
imp-902	cita	2026-07-25	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-22081972	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		t
imp-903	cita	2026-07-25	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1094977327	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		t
imp-904	cita	2026-07-25	11:00:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1037578944	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-905	cita	2026-07-25	11:30:00	12:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1037570796	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		t
imp-906	cita	2026-07-25	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128264708	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-20 00:00:00		t
imp-907	cita	2026-07-25	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43869810	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-24 00:00:00		t
imp-908	cita	2026-07-25	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-123456789	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-909	cita	2026-07-25	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1000534795	est-cancelado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-24 00:00:00		f
imp-91	cita	2026-06-03	14:30:00	15:15:00	esp-manuela-betancur-agudelo-28	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-1000900043	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-02 00:00:00		t
imp-910	cita	2026-07-25	14:30:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1021927920	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-24 00:00:00		t
imp-911	cita	2026-07-25	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1036620763	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-18 00:00:00		t
imp-912	cita	2026-07-25	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-l	cli-52441707	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-21 00:00:00		t
imp-913	cita	2026-07-25	16:30:00	17:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-52441707	est-cumplido	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-21 00:00:00		t
imp-914	cita	2026-07-27	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1090493435	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-24 00:00:00		f
imp-915	cita	2026-07-27	10:00:00	10:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1007353470	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-26 00:00:00		f
imp-916	cita	2026-07-27	10:00:00	10:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1007353470	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-26 00:00:00		f
imp-917	cita	2026-07-27	10:30:00	11:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-39412621	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-918	cita	2026-07-27	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1090493435	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-919	cita	2026-07-27	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017232776	est-realizado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-92	cita	2026-06-04	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-29567472	est-reprogramado	Call Center	ASESOR CC 1 CATALINA JARAMILLO			\N	\N	t	2026-06-01 00:00:00		f
imp-920	cita	2026-07-27	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017126454	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		f
imp-921	cita	2026-07-27	12:00:00	12:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1045017321	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-08 00:00:00		t
imp-922	cita	2026-07-27	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32258349	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-923	cita	2026-07-27	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-1033654796	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		f
imp-924	cita	2026-07-27	15:00:00	15:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1094977327	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-925	cita	2026-07-27	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42979373	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-926	cita	2026-07-27	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43400673	est-incumplido	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-23 00:00:00		t
imp-927	cita	2026-07-27	16:30:00	17:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-masaje-de-relajacion	cli-32258349	est-cancelado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-24 00:00:00		f
imp-928	cita	2026-07-27	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-32258349	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-24 00:00:00		f
imp-929	cita	2026-07-27	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21481522	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-93	cita	2026-06-04	10:00:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1032418627	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-930	cita	2026-07-27	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-63316600	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-931	cita	2026-07-28	09:00:00	09:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1116256148	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-28 00:00:00		t
imp-932	cita	2026-07-28	09:00:00	10:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-42824198	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-22 00:00:00		t
imp-933	cita	2026-07-28	09:30:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1041611004	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-28 00:00:00		t
imp-934	cita	2026-07-28	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-carbon-peel	cli-42824198	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-22 00:00:00		t
imp-935	cita	2026-07-28	11:00:00	11:30:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-123456789	est-reprogramado	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		f
imp-936	cita	2026-07-28	11:00:00	11:20:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-123456789	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		f
imp-937	cita	2026-07-28	11:30:00	11:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-123456789	est-cancelado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-25 00:00:00		f
imp-938	cita	2026-07-28	11:30:00	11:50:00	esp-jorge-ramiro-cueter-guzman-17	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-123456789	est-pendiente	Call Center	ASESOR CC 2 CATALINA JARAMILLO			\N	\N	t	2026-07-01 00:00:00		t
imp-939	cita	2026-07-28	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017932526	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-21 00:00:00		t
imp-94	cita	2026-06-04	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037670965	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-03 00:00:00		f
imp-940	cita	2026-07-28	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-42888483	est-incumplido	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-22 00:00:00		t
imp-941	cita	2026-07-28	14:00:00	14:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-1033654796	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-28 00:00:00		t
imp-942	cita	2026-07-28	14:30:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-xs	cli-1033654796	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-943	cita	2026-07-28	15:00:00	15:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-43253935	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-24 00:00:00		t
imp-944	cita	2026-07-29	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1026251454	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		f
imp-945	cita	2026-07-29	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1039448466	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-946	cita	2026-07-29	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-21831091	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		t
imp-947	cita	2026-07-29	12:00:00	12:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1017126454	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-23 00:00:00		f
imp-948	cita	2026-07-29	12:30:00	13:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128271946	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-06-27 00:00:00		f
imp-949	cita	2026-07-29	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1037610906	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-95	cita	2026-06-04	11:30:00	12:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1125795486	est-reprogramado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-03 00:00:00		f
imp-950	cita	2026-07-29	15:00:00	15:20:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-s	cli-1034993103	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		t
imp-951	cita	2026-07-29	15:30:00	16:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1026251454	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-28 00:00:00		t
imp-952	cita	2026-07-30	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152193761	est-reprogramado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-30 00:00:00		f
imp-953	cita	2026-07-30	13:00:00	13:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1037570253	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		f
imp-954	cita	2026-07-30	13:00:00	13:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-1037570253	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		t
imp-955	cita	2026-07-30	15:00:00	15:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1004997406	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-28 00:00:00		f
imp-956	cita	2026-07-30	16:00:00	16:20:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-cita-de-control-medico	cli-42688945	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-29 00:00:00		t
imp-957	cita	2026-07-30	16:30:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-43868433	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		t
imp-958	cita	2026-07-30	17:00:00	17:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1002642363	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-25 00:00:00		t
imp-959	cita	2026-07-30	17:30:00	18:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-63316600	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-25 00:00:00		f
imp-96	cita	2026-06-04	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1125795486	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-04 00:00:00		t
imp-960	cita	2026-07-31	10:00:00	10:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-43971658	est-reprogramado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-07-29 00:00:00		f
imp-961	cita	2026-07-31	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43746775	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-28 00:00:00		t
imp-962	cita	2026-07-31	11:00:00	11:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrofacial-basica	cli-42828462	est-realizado	Recepcionista	TESORO  CATALINA JARMILLO			\N	\N	t	2026-06-25 00:00:00		t
imp-963	cita	2026-07-31	11:30:00	12:00:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-remocion-micropigmentacion-1-sesion	cli-1004997406	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-28 00:00:00		t
imp-964	cita	2026-07-31	12:00:00	12:30:00	esp-julie-viviana-arias-hernandez-20	sede-cj-medical-el-tesoro	srv-consulta-medica	cli-43971658	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-31 00:00:00		t
imp-965	cita	2026-07-31	14:00:00	14:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1128271946	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-28 00:00:00		t
imp-966	cita	2026-07-31	16:30:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-depilacion-nasal-con-cera	cli-1038262441	est-realizado	Recepcionista	CJMEDICAL * TESORO  CATALINA JARMILLO			\N	\N	t	2026-07-31 00:00:00		t
imp-967	cita	2026-08-01	09:00:00	09:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1022341860	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-04 00:00:00		f
imp-968	cita	2026-08-01	09:30:00	10:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1022341860	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-04 00:00:00		f
imp-969	cita	2026-08-03	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-20387333	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		f
imp-97	cita	2026-06-04	15:00:00	15:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-1-sesion-zona-m	cli-1036607047	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-05-30 00:00:00		f
imp-970	cita	2026-08-03	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1015395409	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-06 00:00:00		f
imp-971	cita	2026-08-03	15:00:00	15:30:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1018456833	est-reprogramado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-972	cita	2026-08-03	15:30:00	16:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1018456833	est-cancelado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-973	cita	2026-08-03	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1000953384	est-reprogramado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-07-17 00:00:00		f
imp-974	cita	2026-08-04	10:30:00	11:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1001854605	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-06-26 00:00:00		f
imp-975	cita	2026-08-04	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52252979	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-07 00:00:00		f
imp-976	cita	2026-08-05	09:00:00	10:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-hidrafacial-plus	cli-51874849	est-cancelado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-07 00:00:00		f
imp-977	cita	2026-08-05	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-978	cita	2026-08-05	12:30:00	13:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-24731927	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-979	cita	2026-08-05	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-26441599	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-14 00:00:00		f
imp-98	cita	2026-06-04	16:00:00	16:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-1152442893	est-realizado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-05-30 00:00:00		t
imp-980	cita	2026-08-06	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1015478534	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-17 00:00:00		f
imp-981	cita	2026-08-06	12:30:00	13:00:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-1102840319	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-07-27 00:00:00		f
imp-982	cita	2026-08-06	16:00:00	16:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-53015367	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-15 00:00:00		f
imp-983	cita	2026-08-08	09:00:00	09:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1018415797	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-984	cita	2026-08-08	09:30:00	10:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52791664	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-985	cita	2026-08-08	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-50922034	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-09 00:00:00		f
imp-986	cita	2026-08-08	10:30:00	11:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52151950	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-987	cita	2026-08-08	11:00:00	11:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-52983883	est-reprogramado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-07-17 00:00:00		f
imp-988	cita	2026-08-08	11:30:00	12:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-carbon-peel	cli-1037644195	est-reprogramado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-989	cita	2026-08-08	12:30:00	12:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-1-sesion-zona-xs	cli-1037644195	est-reprogramado	Recepcionista	CHICO1  CATALINA JARMILLO			\N	\N	t	2026-07-11 00:00:00		f
imp-99	cita	2026-06-04	16:30:00	17:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-terapias-de-revitalizacion	cli-43260411	est-incumplido	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-03 00:00:00		t
imp-990	cita	2026-08-08	13:30:00	14:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1053811453	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-25 00:00:00		f
imp-991	cita	2026-08-08	14:00:00	14:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-carbon-peel	cli-1053811453	est-cancelado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-25 00:00:00		f
imp-992	cita	2026-08-08	15:00:00	15:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1010196637	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-18 00:00:00		f
imp-993	cita	2026-08-11	10:00:00	10:45:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-43869520	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-08 00:00:00		f
imp-994	cita	2026-08-12	16:30:00	17:15:00	esp-laura-marithza-martinez-martinez-23	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-123456789	est-reprogramado	Recepcionista	CJMEDICAL * BOGOTA  CATALINA JARMILLO			\N	\N	t	2026-07-10 00:00:00		f
imp-995	cita	2026-08-13	09:00:00	09:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51976440	est-realizado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-10 00:00:00		t
imp-996	cita	2026-08-13	09:30:00	10:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-l	cli-1020758898	est-reprogramado	Call Center	ASESOR CC 5 CATALINA JARAMILLO			\N	\N	t	2026-08-03 00:00:00		f
imp-997	cita	2026-08-13	10:00:00	10:45:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-1019023831	est-realizado	Call Center	SERVICIO AL CLIENTE  CATALINA JARMILLO			\N	\N	t	2026-08-13 00:00:00		t
imp-998	cita	2026-08-13	10:30:00	11:15:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-terapias-de-revitalizacion	cli-51874849	est-reprogramado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-08-04 00:00:00		f
imp-999	cita	2026-08-13	11:00:00	11:30:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-bogota	srv-1-sesion-zona-m	cli-32780120	est-reprogramado	Call Center	ASESOR CC 4 CATALINA JARAMILLO			\N	\N	t	2026-07-30 00:00:00		f
imp-299	cita	2026-06-18	14:00:00	15:00:00	esp-valentina-rivillas-baquero-42	sede-cj-medical-el-tesoro	srv-hidrafacial-plus	cli-1000084923	est-realizado	Call Center	ASESOR CC 3 CATALINA JARAMILLO			\N	\N	t	2026-06-16 00:00:00		t
\.


--
-- Data for Name: reservas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reservas (id, especialista_id, sede_id, fecha, inicio, fin, canal, referencia, creado_en, expira_en) FROM stdin;
\.


--
-- Name: cita_bitacora_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cita_bitacora_id_seq', 1374, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 5ha7eQcKKEHR607cPYEEaLsw1FPqiMzxSMhgtigODqd7RVcvfdCtkAJQiaqPfGc

