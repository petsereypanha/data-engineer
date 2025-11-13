-- Show all columns in the films table
SELECT column_name, data_type, character_maximum_length, is_nullable
FROM information_schema.columns
WHERE table_name = 'films'
ORDER BY ordinal_position;
