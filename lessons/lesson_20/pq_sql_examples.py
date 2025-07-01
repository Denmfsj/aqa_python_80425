create_table = """CREATE TABLE public."user" (
	id SERIAL,
	name varchar NOT NULL,
	description varchar NULL,
	CONSTRAINT user_pk PRIMARY KEY (id)
);
"""

create_second_table = """
CREATE TABLE public.user_details (
	user_id int NOT NULL,
	phone_number varchar NULL,
	CONSTRAINT user_details_pk PRIMARY KEY (user_id),
	CONSTRAINT user_details_user_fk FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE
);
"""

insert_into = """INSERT INTO public."user" ("name", "description") VALUES ('Den', 'AQA')"""

update = """update public."user" set "name" = 'Alex' where "id" < 4"""

delete = """delete from  public."user" where "id" = 6"""

join = '''select "id", "name", "phone_number"
from "user" inner join "user_details" on "user"."id"="user_details"."user_id"'''