это спец модуль исключеитльно для вызова только из под модуля company
это сделано так как пока неумею рекурсивно запускать модуль company.

 а нужно потому что таблица company имеет у себя форейн кей parent_id который указвает  на эту же таблицу на
столбик company_ip поэтому мне чтобы удалить строку из company с заданным company_id 
надо удалить все строки где на эту строку ссылаеются другие строки у которых parent_id 
указывает на наш company_id  а это же полноценные строки  от которых  завчится нижележаешие таблицы
поэтому чтобы удалить строку нужно удалить другие строки от котрых завяияст нижние таблицы.
вот для удаления заививстмотей в нижних таблицых мы вызываем company2 наделясь что степень вложеннрсти всего одна ступень.

