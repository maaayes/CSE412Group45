--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7 (Homebrew)
-- Dumped by pg_dump version 14.7 (Homebrew)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: albums; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.albums (
    uad integer NOT NULL,
    name character varying,
    uid integer,
    doc date
);


ALTER TABLE public.albums OWNER TO "rootUser";

--
-- Name: comments; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.comments (
    ucd integer NOT NULL,
    text character varying,
    userid integer,
    upd integer,
    dateleft date
);


ALTER TABLE public.comments OWNER TO "rootUser";

--
-- Name: friends; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.friends (
    userid integer NOT NULL,
    friend integer,
    friendshipdate date
);


ALTER TABLE public.friends OWNER TO "rootUser";

--
-- Name: likes; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.likes (
    upd integer NOT NULL,
    userid integer,
    likecount integer
);


ALTER TABLE public.likes OWNER TO "rootUser";

--
-- Name: photos; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.photos (
    upd integer NOT NULL,
    uad integer,
    caption character varying,
    data character varying,
    filepath character varying
);


ALTER TABLE public.photos OWNER TO "rootUser";

--
-- Name: tags; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.tags (
    tag character varying,
    upd integer NOT NULL
);


ALTER TABLE public.tags OWNER TO "rootUser";

--
-- Name: users; Type: TABLE; Schema: public; Owner: rootUser
--

CREATE TABLE public.users (
    userid integer NOT NULL,
    fname character varying,
    lname character varying,
    email character varying,
    dob date,
    hometown character varying,
    gender character varying,
    password character varying,
    albumnum integer
);


ALTER TABLE public.users OWNER TO "rootUser";

--
-- Data for Name: albums; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.albums (uad, name, uid, doc) FROM stdin;
\.


--
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.comments (ucd, text, userid, upd, dateleft) FROM stdin;
\.


--
-- Data for Name: friends; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.friends (userid, friend, friendshipdate) FROM stdin;
\.


--
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.likes (upd, userid, likecount) FROM stdin;
\.


--
-- Data for Name: photos; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.photos (upd, uad, caption, data, filepath) FROM stdin;
\.


--
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.tags (tag, upd) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: rootUser
--

COPY public.users (userid, fname, lname, email, dob, hometown, gender, password, albumnum) FROM stdin;
1	aba	aba	2@gmail.co	2023-04-23	cshu	Male	2	0
\.


--
-- Name: albums albums_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.albums
    ADD CONSTRAINT albums_pkey PRIMARY KEY (uad);


--
-- Name: albums albums_uid_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.albums
    ADD CONSTRAINT albums_uid_key UNIQUE (uid);


--
-- Name: comments comments_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (ucd);


--
-- Name: comments comments_upd_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_upd_key UNIQUE (upd);


--
-- Name: comments comments_userid_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_userid_key UNIQUE (userid);


--
-- Name: friends friends_friend_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.friends
    ADD CONSTRAINT friends_friend_key UNIQUE (friend);


--
-- Name: friends friends_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.friends
    ADD CONSTRAINT friends_pkey PRIMARY KEY (userid);


--
-- Name: likes likes_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pkey PRIMARY KEY (upd);


--
-- Name: likes likes_userid_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_userid_key UNIQUE (userid);


--
-- Name: photos photos_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.photos
    ADD CONSTRAINT photos_pkey PRIMARY KEY (upd);


--
-- Name: photos photos_uad_key; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.photos
    ADD CONSTRAINT photos_uad_key UNIQUE (uad);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (upd);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: rootUser
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (userid);


--
-- PostgreSQL database dump complete
--

